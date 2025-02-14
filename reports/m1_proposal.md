# Proposal

## Section 1: Motivation and Purpose

Our role: Data Scientist Consultancy Firm

Target audience: Car buyers & automotive enthusiasts

Buying a car is a significant decision that takes multiple factors into account. Many buyers struggle to navigate vast amounts of data and make informed choices that best suit their needs. To address this challenge, we propose building an interactive car comparison dashboard that allows users to visually explore and compare different vehicle models in the market based on key specifications. Our dashboard will feature dynamic filters and visualizations, enabling users to adjust criteria such as price range, horsepower, fuel type, and seating capacity to find the best options. By providing an intuitive and interactive experience, our tool aims to simplify car selection and empower buyers with data-driven insights.

## Section 2: Description of the data

We are using the Ultimate Cars Dataset 2024 from Kaggle, featuring car specifications, performance metrics, pricing, etc.

### Dataset Overview

- **Total Rows:** 1,213
- **Total Columns:** 11
- **Data Source:** [The Ultimate Cars Dataset 2024](https://www.kaggle.com/datasets/abdulmalik1518/the-ultimate-cars-dataset-2024)

### Key Variables for Visualization

1. **Vehicle Specifications:**
   - `Company Names`: The brand/manufacturer of the vehicle.
   - `Cars Names`: The model name of the vehicle.
   - `Engines`: Engine type (e.g., V8, V12, Electric).
   - `CC/Battery Capacity`: The engine displacement or battery capacity for electric vehicles.
   - `HorsePower`: The vehicle's horsepower.
   - `Total Speed`: The top speed of the vehicle.
   - `Performance(0 - 100 KM/H)`: The acceleration time from 0 to 100 km/h.
   - `Torque`: The amount of torque (Nm) produced by the vehicle.

2. **Pricing and Fuel Information:**
   - `Cars Prices`: The listed price range (USD) of the vehicle.
   - `Fuel Types`: The type of fuel used (e.g., Petrol, Electric, Hybrid).
   - `Seats`: The number of seats in the vehicle.

### Data Engineering and New Variables

To enhance the insights provided by our dashboard, we plan to derive the following new variables:

- **Performance-to-Price Ratio:** A calculated metric to compare horsepower relative to the price.
- **Vehicle Segmentation:** Grouping cars into categories based on their seats and fuel types.

### Justification for Dataset Choice

The dataset offers detailed car specs from various manufacturers, making it ideal for our dashboard. Users can:

- Compare car models based on speed, horsepower, and acceleration.
- Filter vehicles by price, fuel type, and seating capacity to find suitable options.
- Identify trends across different manufacturers and price categories.

With dynamic filters and comparisons, the dashboard simplifies decision-making for car buyers and provides valuable insights for automotive enthusiasts.

**Reference:**

Abdulmalik, A. (2024). The Ultimate Cars Dataset 2024 [Data set]. Kaggle. Retrieved from https://www.kaggle.com/datasets/abdulmalik1518/the-ultimate-cars-dataset-2024.

## Section 3: Research questions and usage scenarios

### Research questions

The following research questions will guide the interactive analysis of this dashboard:

- How do car prices vary across different manufacturers and fuel types?  - to capture price variation by model
- How is the distribution of battery capacity (for EVs) or engine CC (for fuel cars) across car types? - Captures performance variations
- What are the top car models by manufacturer? - Captures market concentration
- How does seating capacity influence price and fuel type choices?  - to capture vehicle size variations
- How do horsepower, performance, and total speed influence pricing? - Conditional price filters
- What is the distribution of horsepower and price across different car types and fuel types?

### Usage Scenario

#### Scenario 1: Car Buyers

Emily is a mother of two looking for a spacious and safe vehicle to accommodate her kids and their belongings. With frequent weekend trips to Whistler and interior BC, she needs a car with good highway performance and cargo space.  

Emily wants to find a family-friendly vehicle with ample seating, cargo space, and good safety features while staying within a budget.  

**Tasks:**

**[Filter]** by seating capacity (5+ seats) and price range ($30,000 - $50,000).

**[Compare]** SUVs and minivans by fuel type (prioritizing hybrid/electric).

**[Check]** performance metrics (horsepower and total speed) for highway travel.

Emily opens VDash and applies all the conditions. The dashboard dynamically updates, showing available options with key performance metrics like horsepower, performance, and total speed. The dashboard highlights hybrid SUVs with strong horsepower and speed. She selects a few options and plans test drives.

#### Scenario 2: Automotive Manufacturer (Product Manager)

Sophia is a Product Manager at a global automotive manufacturer. She needs to analyze how her company's vehicles compare to competitors in terms of price, performance, and fuel type to identify areas for improvement.

**Tasks:**

**[Filter]** by company, fuel type, and vehicle category.

**[Compare]** price and performance metrics (horsepower, speed) across competitors.

**[Identify]** gaps in pricing or performance for specific models.

When Sophia opens the dashboard, she views price distribution, horsepower, and speed across vehicle types, fuel types, and brands. She filters the data by company, fuel type, and vehicle category to compare her company’s cars with competitors.

Exploring hybrid vehicles, Sophia notices her company's model is priced higher but offers superior horsepower and speed—a strong selling point for premium consumers seeking performance and sustainability. She decides to emphasize these features in marketing.

Next, she compares mid-range sedans and finds their horsepower lags behind certain competitors, despite competitive pricing. This prompts her to request a review of engineering priorities to boost horsepower while maintaining costs.

Using the dashboard’s filter and compare features, Sophia identifies models offering more performance for a similar price and considers price adjustments or performance improvements to enhance value for customers.

## Section 4: App sketch & brief description

-TO DO-
