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

# Price range input boxes (default to CAD)
min_price_input = dcc.Input(
    id="min-price-input",
    type="number",
    value=min_price_cad
)

max_price_input = dcc.Input(
    id="max-price-input",
    type="number",
    value=max_price_cad
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
