import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import src.callbacks
from src.components import (
    currency_switch_btns,
    overview_company_dropdown,
    details_company_dropdown,
    fuel_types_dropdown,
    car_types_dropdown,
    price_range_slider,
    min_price_input,
    max_price_input,
    total_speed_range_slider,
    min_total_speed_input,
    max_total_speed_input,
    seats_range_slider,
    min_seats_input,
    max_seats_input,
    max_speed_horsepower
)

# Initialize Dash App with Bootstrap Theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# HEADER SECTION
header = dbc.Navbar(
    dbc.Container([
        html.Div([
            html.Img(src="assets/logo.png", height="50px", className="me-3"),
            html.H1("VDash: Speed Up Your Car Hunt", className="text-light fw-bold")
        ], className="d-flex align-items-center"),
        currency_switch_btns  # CAD/USD Switch
    ], fluid=True),
    color="dark", dark=True, className="mb-4 p-3"
)

# COMPANY OVERVIEW SECTION
company_overview = dbc.Card([
    dbc.CardHeader(html.H4("📊 Company Overview", className="fw-bold")),
    dbc.CardBody([
        # Company Dropdown
        overview_company_dropdown,

        # Bar Chart & Histogram
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    id="max-speed-hp-card",
                    className="metric-box p-3",
                )
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H5("Number of Car Models by Company", className="text-center fw-bold"),
                    dvc.Vega(id='cars-bar-chart')
                ], style={"textAlign": "center"})
            ], width=5),
            dbc.Col([
                html.Div([
                    html.H5("Car Price Distribution", className="text-center fw-bold"),
                    dvc.Vega(id='price-range-histogram')
                ], style={"textAlign": "center"})
            ], width=5)
        ])
    ])
], className="p-3")

# DETAILED ANALYSIS - FILTERS (SIDEBAR)
sidebar = dbc.Card([
    dbc.CardHeader(html.H4("📊 Detailed Analysis", className="fw-bold")),

    dbc.CardBody([
        html.Label("Select companies:", className="fw-bold"),
        details_company_dropdown,

        html.Label("Select fuel types:", className="fw-bold"),
        fuel_types_dropdown,

        html.Label("Select car types:", className="fw-bold"),
        car_types_dropdown,

        html.Label("Select price range:", className="fw-bold"),
        price_range_slider,
        html.Div([min_price_input, max_price_input], className="d-flex justify-content-between"),
        html.P(id="currency-label", className="text-muted text-end"),

        html.Label("Select total speed range:", className="fw-bold"),
        total_speed_range_slider,
        html.Div([min_total_speed_input, max_total_speed_input], className="d-flex justify-content-between"),
        html.P("km/h", className="text-muted text-end"),

        html.Label("Select seat numbers:", className="fw-bold"),
        seats_range_slider,
        html.Div([min_seats_input, max_seats_input], className="d-flex justify-content-between"),
        html.P("Seats", className="text-muted text-end"),
    ])
], body=True, className="p-3")

# DETAILED ANALYSIS - CHARTS
scatter_plot_card = dbc.Card([
    html.H5(id="scatter-plot-title", className="text-center fw-bold"),
    dvc.Vega(id="scatter-plot"),
    dcc.RadioItems(
        id="scatter-toggle",
        options=[
            {"label": "Horsepower", "value": "horsepower"},
            {"label": "Performance", "value": "performance_0_100_km/h"},
            {"label": "Total speed", "value": "total_speed"},
        ],
        value="horsepower",
        inline=True,
        className="mt-2 d-flex justify-content-center",
    ),
], body=True, className="p-3")

price_boxplot_card = dbc.Card([
    html.H5(id="price-boxplot-title", className="text-center fw-bold"),
    dvc.Vega(id="price-boxplot"),
    dcc.RadioItems(
        id="boxplot-category-radio1",
        options=[
            {"label": "Company", "value": "company_names"},
            {"label": "Fuel type", "value": "fuel_types_cleaned"},
        ],
        value="fuel_types_cleaned", inline=True, className="mt-2 d-flex justify-content-center",
    ),
], body=True, className="p-3")

horsepower_boxplot_card = dbc.Card([
    html.H5(id="horsepower-boxplot-title", className="text-center fw-bold"),
    dvc.Vega(id="horsepower-boxplot"),
    dcc.RadioItems(
        id="boxplot-category-radio2",
        options=[
            {"label": "Company", "value": "company_names"},
            {"label": "Fuel type", "value": "fuel_types_cleaned"},
        ],
        value="company_names", inline=True, className="mt-2 d-flex justify-content-center",
    ),
], body=True, className="p-3")

# MAIN LAYOUT
app.layout = dbc.Container([
    header,

    # Company Overview Section
    dbc.Row([
        dbc.Col(company_overview, width=12)
    ], className="mb-4"),

    # Detailed Analysis Section (Filters & Charts)
    dbc.Row([
        dbc.Col(sidebar, width=3),
        dbc.Col(scatter_plot_card, width=3),
        dbc.Col(price_boxplot_card, width=3),
        dbc.Col(horsepower_boxplot_card, width=3),
    ], className="g-3"),
], fluid=True)

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)