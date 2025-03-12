import os
import pandas as pd
import numpy as np
import kagglehub
import shutil
import joblib

memory = joblib.Memory("cache", verbose=0)

# Set up directories for data storage
def setup_directories():
    os.makedirs("data/raw/", exist_ok=True)
    os.makedirs("data/processed/", exist_ok=True)

    return {
        "raw_dir": "data/raw/",
        "processed_dir": "data/processed/",
        "raw_file": "data/raw/ultimate_cars_dataset_2024.csv",
        "processed_file": "data/processed/cleaned_cars_df.csv",
        "processed_parquet_file": "data/processed/cleaned_cars_df.parquet"
    }


# Download the car dataset from Kaggle
def download_dataset(paths):
    if os.path.exists(paths["raw_file"]):
        print(f"Dataset already exists at {paths['raw_file']}")
        return

    print("Downloading dataset from Kaggle...")
    download_path = kagglehub.dataset_download("abdulmalik1518/the-ultimate-cars-dataset-2024")

    if not os.path.exists(download_path):
        raise FileNotFoundError(f"Download path {download_path} does not exist.")

    # Find and move the CSV file
    for file_name in os.listdir(download_path):
        if file_name.endswith(".csv"):
            old_file_path = os.path.join(download_path, file_name)
            shutil.copy(old_file_path, paths["raw_file"])
            print(f"Dataset downloaded and copied to {paths['raw_file']}")
            return
    raise FileNotFoundError("CSV file not found in the downloaded dataset.")


# Extract the minimum value from a range or clean numeric data
def extract_min_value(value):
    if pd.isna(value):
        return value

    value = str(value).lower()
    for term in ["cc", "~", "hp", "km/h", "sec", "nm", "$", ","]:
        value = value.replace(term, "")
    value = value.strip()

    if '-' in value:
        return float(value.split('-')[0])  # Take minimum value in range

    try:
        return float(value)
    except ValueError:
        return None


# Clean the battery capacity column
def clean_capacity(s):
    if isinstance(s, str):
        return s.replace(',', '').replace('"', '').strip()
    return s


# Categorize car types based on multiple attributes
def categorize_car_type(row):
    fuel_type = str(row['fuel_types']).lower()
    seats = row['seats']
    horsepower = row['horsepower']
    speed = row['total_speed']
    performance = row['performance_0_100_km/h']
    engines = str(row['engines']).lower()

    # Sports car logic
    if (
        'race' in row['cars_names'].lower() or
        ('v8' in engines and seats <= 4) or
        ('v12' in engines and seats <= 4) or 
        (performance <= 4) or
        (speed >= 240 and (seats <= 4 or pd.isna(seats))) or
        (horsepower >= 450 and (seats <= 4 or pd.isna(seats))) or
        (horsepower >= 350 and (seats <= 2 or pd.isna(seats)))
    ):
        return 'sports'

    # Coupe car logic
    if (
        ('coupe' in row['cars_names'].lower()) or
        (seats <= 2 and horsepower >= 200)
    ):
        return 'coupe'

    # Sedan car logic
    if (
        (2 <= seats <= 5 and horsepower >= 100)
    ):
        return 'sedan'

    # Bus/Truck logic
    if (
        ('diesel' in fuel_type and seats > 7) or
        'pickup' in row['cars_names'].lower() or
        'truck' in row['cars_names'].lower() or
        'bus' in row['cars_names'].lower()
    ):
        return 'bus/truck'

    # SUV logic
    if (
        (5 <= seats <= 7 and horsepower >= 100)
    ):
        return 'suv'

    # Others
    return 'others'


# Clean and transform the raw car data
@memory.cache()
def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=True).str.replace(r"[()\[\]]", "", regex=True)

    # Extract numeric values for CC/Battery Capacity
    df['cc_battery_capacity'] = df['cc/battery_capacity'].astype(str)
    df['battery_capacity_kwh'] = df['cc_battery_capacity'].str.extract(r'([\d.]+)\s*kwh', expand=False).astype(float)
    df['cc_capacity'] = df['cc_battery_capacity'].str.extract(r'([\d.]+)\s*cc', expand=False).astype(float)

    # Create a binary indicator for electric vehicles
    df['is_electric'] = df['battery_capacity_kwh'].notna().astype(int)

    # Fill missing values appropriately
    df['cc_capacity'] = df['cc_capacity'].fillna(0)
    df['battery_capacity_kwh'] = df['battery_capacity_kwh'].fillna(0)

    # Apply cleaning to numerical columns
    df['horsepower'] = df['horsepower'].apply(extract_min_value)
    df['total_speed'] = df['total_speed'].apply(extract_min_value)
    df['performance_0_100_km/h'] = df['performance0_-_100_km/h'].apply(extract_min_value)
    df['torque'] = df['torque'].apply(extract_min_value)
    df['cars_prices'] = df['cars_prices'].apply(extract_min_value)

    df['seats'] = pd.to_numeric(df['seats'], errors='coerce')

    # Fill missing numerical values with mean where applicable
    df['torque'] = df['torque'].fillna(df['torque'].mean())
    df['performance_0_100_km/h'] = df['performance_0_100_km/h'].fillna(df['performance_0_100_km/h'].mean())

    # Drop unnecessary columns
    df.drop(columns=['cc/battery_capacity', 'performance0_-_100_km/h'], inplace=True)

    # Currency Conversion
    conversion_rate = 1.35  # 1 USD = 1.35 CAD
    df['cars_prices_cad'] = (df['cars_prices'] * conversion_rate).round(1)
    df['cars_prices_usd'] = df['cars_prices'].round(1)

    # Categorize fuel types
    gas_pattern = r'cng|petrol|diesel|awd'
    hybrid_pattern = r'plug-in|hyrbrid|hybrid'
    electric_pattern = r'electric|ev|hydrogen'

    conditions = [
        df['fuel_types'].str.contains(gas_pattern, case=False, regex=True),
        df['fuel_types'].str.contains(hybrid_pattern, case=False, regex=True),
        df['fuel_types'].str.contains(electric_pattern, case=False, regex=True)
    ]

    choices = ['gas', 'hybrid', 'electric']
    df['fuel_types_cleaned'] = np.select(conditions, choices, default='unknown')

    # Apply car type categorization
    df['car_types'] = df.apply(categorize_car_type, axis=1)

    # Drop missing values
    cleaned_df = df.dropna()

    # Clean battery capacity column
    cleaned_df = cleaned_df.copy()
    cleaned_df['cc_battery_capacity'] = cleaned_df['cc_battery_capacity'].apply(clean_capacity)

    # Remove redundant columns
    cols_to_drop = ['cars_prices', 'fuel_types', 'battery_capacity_kwh', 
                    'cc_capacity', 'is_electric', 'torque', 'engines']
    cleaned_df = cleaned_df.drop(columns=cols_to_drop)

    # Fix company names
    cleaned_df['company_names'] = cleaned_df['company_names'].str.strip()

    # Standardize inconsistent brands
    fix_mappings = {
        'ROLLS ROYCE ': 'ROLLS ROYCE',
        'Nissan': 'NISSAN',
        'Volvo': 'VOLVO',
        'KIA  ': 'KIA',
        'Kia': 'KIA'
    }
    cleaned_df['company_names'] = cleaned_df['company_names'].replace(fix_mappings)

    # Capitalize the 'car_types' and 'fuel_types_cleaned' columns
    cleaned_df['car_types'] = cleaned_df['car_types'].str.capitalize()
    cleaned_df['fuel_types_cleaned'] = cleaned_df['fuel_types_cleaned'].str.capitalize()

    # Reorder and delete unused columns
    reordered_cols = [
        'company_names', 'cars_names', 'car_types', 'fuel_types_cleaned', 'cc_battery_capacity',
        'horsepower', 'total_speed', 'performance_0_100_km/h', 'seats', 'cars_prices_cad', 'cars_prices_usd'
    ]

    return cleaned_df[reordered_cols]


# Prepare data for the dashboard
@memory.cache()
def prepare_data():
    paths = setup_directories()
    
    # Check if processed parquet data already exists
    if os.path.exists(paths["processed_parquet_file"]):
        print(f"Loading processed data from {paths['processed_parquet_file']}")
        return pd.read_parquet(paths["processed_parquet_file"])

    # Download and process data
    download_dataset(paths)

    # Load and clean the data
    print("Processing data...")
    raw_df = pd.read_csv(paths["raw_file"], encoding="ISO-8859-1")
    cleaned_df = clean_data(raw_df)

    # Save processed data in both CSV (for readability) and Parquet (for performance)
    cleaned_df.to_csv(paths["processed_file"], index=False)
    cleaned_df.to_parquet(paths["processed_parquet_file"], index=False)
    print(f"Processed data saved to CSV: {paths['processed_file']}")
    print(f"Processed data saved to Parquet: {paths['processed_parquet_file']}")

    return cleaned_df


# Load the car data for the dashboard
cars_df = prepare_data()

# For debugging/testing
if __name__ == "__main__":
    print(f"Loaded {len(cars_df)} car records")
    print(f"Sample data:\n{cars_df.head()}")
    print(f"Data types:\n{cars_df.dtypes}")
    print(f"Unique companies: {cars_df['company_names'].nunique()}")
    print(f"Unique car types: {cars_df['car_types'].unique()}")
