import altair as alt
import pandas as pd
from dash import html, dcc
from .data import cars_df

min_price_cad = cars_df['cars_prices_cad'].min()  # 5,400
max_price_cad = cars_df['cars_prices_cad'].max()  # 24,300,000
min_price_usd = cars_df['cars_prices_usd'].min()  # 4,000
max_price_usd = cars_df['cars_prices_usd'].max()  # 18,000,000
min_total_speed = cars_df['total_speed'].min()  # 80.0
max_total_speed = cars_df['total_speed'].max()  # 500.0
min_seats = cars_df['seats'].min()  # 1
max_seats = cars_df['seats'].max()  # 20

# ============ INPUTS ============

# Currency switch buttons
currency_switch_btns = html.Div([
    html.Button("CAD", id="currency-cad-btn", n_clicks=0, className="active-btn"),
    html.Button("USD", id="currency-usd-btn", n_clicks=0, className="inactive-btn"),
])

# Overview company dropdown multi-selector
overview_company_dropdown = dcc.Dropdown(
    id='overview-company-dropdown',
    options=sorted(cars_df['company_names'].unique()),
    value=['AUDI', 'BMW', 'Ford', 'Mazda', 'TOYOTA'],
    multi=True,
    placeholder='Select up to 5 companies...'
)

# Detailed analysis company dropdown multi-selector
details_company_dropdown = dcc.Dropdown(
    id='details-company-dropdown',
    options=sorted(cars_df['company_names'].unique()),
    value=['AUDI', 'BMW', 'Tesla'],
    multi=True,
    placeholder='Select up to 5 companies...'
)

# Fuel types dropdown multi-selector
fuel_types_dropdown = dcc.Dropdown(
    id='fuel-types-dropdown',
    options=sorted(cars_df['fuel_types_cleaned'].unique()),
    value=['Electric', 'Gas', 'Hybrid'],
    multi=True,
    placeholder='Select fuel types...'
)

# # Car type dropdown multi-selector
# car_types_dropdown = dcc.Dropdown(
#     id='car-types-dropdown',
#     options=sorted(cars_df['car_types'].unique()),
#     value=sorted(cars_df['car_types'].dropna().unique()),
#     multi=True,
#     placeholder='Select car types...'
# )


# Price range input boxes (default to CAD)
min_price_input = dcc.Input(
    id="min-price-input", 
    type="number", 
    value=min_price_cad,
    min=min_price_cad, 
    max=max_price_cad, 
    step=100
)

max_price_input = dcc.Input(
    id="max-price-input", 
    type="number", 
    value=max_price_cad, 
    min=min_price_cad, 
    max=max_price_cad, 
    step=100
)

# Price range slider (default to CAD)
price_range_slider = dcc.RangeSlider(
    id="price-range-slider",
    min=min_price_cad,
    max=max_price_cad,
    step=100,
    value=[min_price_cad, max_price_cad],
    pushable=1000,
    marks=None,
    tooltip={"placement": "bottom"}
)

# Total speed range input boxes
min_total_speed_input = dcc.Input(
    id="min-total-speed-input",
    type="number",
    value=min_total_speed
)

max_total_speed_input = dcc.Input(
    id="max-total-speed-input",
    type="number",
    value=max_total_speed
)

# Total speed range slider
total_speed_range_slider = dcc.RangeSlider(
    id="total-speed-range-slider",
    min=min_total_speed,
    max=max_total_speed,
    step=10,
    value=[min_total_speed, max_total_speed],
    pushable=10,
    marks=None,
    tooltip={"placement": "bottom"}
)

# Seat numbers input boxes
min_seats_input = dcc.Input(
    id="min-seats-input",
    type="number",
    value=min_seats
)

max_seats_input = dcc.Input(
    id="max-seats-input",
    type="number",
    value=max_seats
)

# Seat numbers range slider
seats_range_slider = dcc.RangeSlider(
    id="seats-range-slider",
    min=min_seats,
    max=max_seats,
    step=1,
    value=[min_seats, max_seats],
    pushable=1,
    tooltip={"placement": "bottom"}
)


# ============ OUTPUTS ============


# Card: Max total speed & horsepower within selected companies
def max_speed_horsepower(df):
    if df.empty:
        return None, None

    max_speed = df['total_speed'].max()
    max_hp = df['horsepower'].max()

    return max_speed, max_hp


# Bar chart: number of car models in each company
def plot_bar_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('count()', title='Number of Car Models'),
        y=alt.Y('company_names:N', title='Company'),
        tooltip=[
            alt.Tooltip('company_names:N', title='Company'), 
            alt.Tooltip('count()', title='Count')
        ]
    ).properties(
        width=700,
        height=350
    ).interactive().to_dict(format="vega")

    return chart


# Histogram: car price range histogram for selected company
def plot_grouped_histogram(df, currency='CAD'):
    if currency == 'CAD':
        price_column = 'cars_prices_cad'
        price_bins = [0, 20000, 30000, 50000, 80000, 100000, float('inf')]
        price_labels = ["0-20K", "20-30K", "30-50K", "50-80K", "80-100K", "100K+"]
        x_title = "Price Range (CAD)"
    else:  # USD
        price_column = 'cars_prices_usd'
        price_bins = [0, 15000, 22000, 37000, 60000, 75000, float('inf')]
        price_labels = ["0-15K", "15-22K", "22-37K", "37-60K", "60-75K", "75K+"]
        x_title = "Price Range (USD)"

    # Bin the price column into categories
    df = df.copy()
    df['Price Range'] = pd.cut(
        df[price_column],
        bins=price_bins,
        labels=price_labels,
        right=False
    )

    # Get car names, limiting to 14 entries to prevent tooltip overflow
    grouped_df = df.groupby(['Price Range', 'company_names']).agg(
        count=('cars_names', 'count'),
        cars_names=('cars_names', lambda x: list(x.dropna().astype(str)))
    ).reset_index()

    grouped_df['cars_names'] = grouped_df['cars_names'].apply(
        lambda x: ', '.join(x[:14]) + '...' if isinstance(x, list) and len(x) > 14 else ', '.join(x) if isinstance(x, list) else ''
    )

    chart = alt.Chart(grouped_df).mark_bar().encode(
        x=alt.X('Price Range:N', title=x_title, sort=price_labels),
        y=alt.Y('count:Q', title="Number of Car Models"),
        color=alt.Color('company_names:N', title="Company"),
        xOffset='company_names:N',
        tooltip=[
            alt.Tooltip('company_names:N', title="Company"),
            alt.Tooltip('count:Q', title="Car Count"),
            alt.Tooltip('cars_names:N', title="Car Models")
        ]
    ).properties(
        width=700,
        height=350
    ).configure_axisX(
        labelAngle=0
    ).to_dict(format="vega")

    return chart


# horsepower_price scatter plot
def horsepower_price(filtered_df, x_var, price_col):
    x_max = filtered_df[x_var].max() * 1.05
    price_max = filtered_df[price_col].max() * 1.05

    x_title_map = {
        "horsepower": "Horse Power",
        "performance_0_100_km/h": "Performance (0-100 km/h)",
        "total_speed": "Total Speed (km/h)"
    }
    x_title = x_title_map.get(x_var, "Horse Power")
    y_title = "Price (CAD)" if price_col == "cars_prices_cad" else "Price (USD)"

    chart = (
        alt.Chart(filtered_df)
        .mark_circle(size=80, opacity=0.8)
        .encode(
            x=alt.X(
                x_var,
                title=x_title,
                scale=alt.Scale(
                    domain=[0, x_max],
                    nice=True
                ),
                axis=alt.Axis(grid=True)
            ),
            y=alt.Y(
                price_col,
                title=y_title,
                scale=alt.Scale(
                    domain=[0, price_max],
                    nice=True
                ),
                axis=alt.Axis(grid=True)
            ),
            color=alt.Color("company_names", legend=alt.Legend(title="Company")),
            tooltip=[
                alt.Tooltip("cars_names:N", title="Car Name"),
                alt.Tooltip("company_names:N", title="Company"),
                alt.Tooltip("fuel_types_cleaned:N", title="Fuel Type"),
                alt.Tooltip(price_col, title=y_title),
                alt.Tooltip(x_var, title=x_title),
                alt.Tooltip("cc_battery_capacity", title="CC/Battery Capacity"),
                alt.Tooltip("seats", title="Seats"),
                alt.Tooltip("car_types", title="Car Type"),
            ]
        )
        .properties(width=300, height=450)
        .interactive()
    )

    return chart


# Boxplot: car price distribution with category selection
def plot_boxplot_price(df, category="company_names", price_col="cars_prices_cad", min_price=None, max_price=None):

    if df.empty:
        return empty_warning_plot()

    if category not in df.columns:
        category = "company_names"

    category_labels = {
        "company_names": "Company",
        "fuel_types_cleaned": "Fuel Type"
    }
    display_name = category_labels.get(category, category.replace("_", " ").title())

    if min_price is not None and max_price is not None:
        df = df[(df[price_col] >= min_price) & (df[price_col] <= max_price)]

    summary_df = df.groupby(category)[price_col].describe().reset_index()
    summary_df = summary_df.rename(columns={"25%": "Q1", "50%": "Median", "75%": "Q3"})

    boxplot = alt.Chart(df).mark_boxplot().encode(
        x=alt.X(f"{category}:N",
                title=display_name,
                axis=alt.Axis(labelAngle=-360)),
        y=alt.Y(f"{price_col}:Q",
                title="Price (CAD)" if price_col == "cars_prices_cad" else "Price (USD)"),
        color=alt.Color(f"{category}:N",
                        title=display_name,
                        legend=alt.Legend(title=display_name))
    )

    whisker = alt.Chart(summary_df).mark_rule().encode(
        x=alt.X(f"{category}:N", title=display_name),
        y=alt.Y("min:Q"),
        tooltip=[
            alt.Tooltip(f"{category}:N", title=display_name),
            alt.Tooltip("max:Q", title="Max"),
            alt.Tooltip("Q3:Q", title="75% (Q3)"),
            alt.Tooltip("median:Q", title="Median"),
            alt.Tooltip("Q1:Q", title="25% (Q1)"),
            alt.Tooltip("min:Q", title="Min")
        ]
    )

    price_boxplot = alt.layer(boxplot, whisker).properties(
        width=300,
        height=450
    ).to_dict(format="vega")

    return price_boxplot


# Empty plot: shows when no data avaliable
def empty_warning_plot():
    return alt.Chart().mark_text(
        text="No data available",
        fontSize=14,
    ).properties(
        width=300, height=450
    ).to_dict()


# Boxplot: Horsepower distribution with category selection
def plot_boxplot_horsepower(df, category="company_names"):
    df = df[df['horsepower'].notna()]
    if df.empty:
        return {}

    if category not in df.columns:
        category = "company_names"

    category_labels = {
        "company_names": "Company",
        "fuel_types_cleaned": "Fuel Type"
    }
    display_name = category_labels.get(category, category.replace("_", " ").title())

    # Calculate Boxplot statistics
    summary_df = df.groupby(category).agg(
        Min=('horsepower', 'min'),
        Q1=('horsepower', lambda x: x.quantile(0.25)),
        Median=('horsepower', 'median'),
        Q3=('horsepower', lambda x: x.quantile(0.75)),
        Max=('horsepower', 'max')
    ).reset_index()

    # Whiskers (Min and Max)
    whiskers = alt.Chart(summary_df).mark_rule().encode(
        x=alt.X(f'{category}:N', title=display_name, axis=alt.Axis(labelAngle=-360)),
        y=alt.Y('Min:Q', title="Horsepower"),
        y2='Max:Q',
        tooltip=[
            alt.Tooltip('Max:Q', title="Max"),
            alt.Tooltip('Q3:Q', title="75%"),
            alt.Tooltip('Median:Q', title="Median"),
            alt.Tooltip('Q1:Q', title="25%"),
            alt.Tooltip('Min:Q', title="Min"),
            alt.Tooltip(f'{category}:N', title=display_name)
        ]
    )

    # Boxplot
    box = alt.Chart(summary_df).mark_bar(size=20, opacity=0.6).encode(
        x=alt.X(f'{category}:N'),
        y=alt.Y('Q1:Q'),
        y2='Q3:Q',
        color=alt.Color(f'{category}:N', title=display_name, legend=alt.Legend(title=display_name)),
        tooltip=[
            alt.Tooltip('Max:Q', title="Max"),
            alt.Tooltip('Q3:Q', title="75%"),
            alt.Tooltip('Median:Q', title="Median"),
            alt.Tooltip('Q1:Q', title="25%"),
            alt.Tooltip('Min:Q', title="Min"),
            alt.Tooltip(f'{category}:N', title="Category")
        ]
    )

    # Median Tick
    median_tick = alt.Chart(summary_df).mark_tick(
        color='black',
        size=40
    ).encode(
        x=alt.X(f'{category}:N'),
        y=alt.Y('Median:Q'),
        tooltip=[
            alt.Tooltip('Median:Q', title="Median"),
            alt.Tooltip(f'{category}:N', title=display_name)
        ]
    )

    # Whiskers + Box + Median Tick
    chart = (whiskers + box + median_tick).properties(
        width=300,
        height=450
    ).to_dict(format="vega")

    return chart
