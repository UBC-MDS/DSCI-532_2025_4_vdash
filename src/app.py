import sys
import os
from datetime import datetime
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
server = app.server

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

# COMPANY OVERVIEW - FILTERS (SIDEBAR)
company_sidebar = dbc.Card([
    dbc.CardHeader(html.H4("Company Selection", className="fw-bold")),
    dbc.CardBody([
        html.Label("Select company:", className="fw-bold"),
        overview_company_dropdown,
        html.Div([
            dbc.Card(
                id="max-speed-hp-card",
                className="metric-box p-3 mt-4",
            )
        ])
    ])
], body=True, className="p-3 h-100")

# COMPANY OVERVIEW - CHARTS
bar_chart_card = dbc.Card([
    html.Div([
        html.H6("Number of Car Models by Company", className="fw-bold text-center mb-3"),
        dvc.Vega(id='cars-bar-chart')
    ], className="d-flex flex-column justify-content-center align-items-center h-100")
], body=True, className="p-3 h-100")

histogram_card = dbc.Card([
    html.Div([
        html.H6("Car Price Distribution", className="fw-bold text-center mb-3"),
        dvc.Vega(id='price-range-histogram', className="align-self-start ms-2")
    ], className="d-flex flex-column justify-content-center align-items-center h-100")
], body=True, className="p-3 h-100")

# DETAILED ANALYSIS - FILTERS (SIDEBAR)
sidebar = dbc.Card([
    dbc.CardHeader(html.H4("Detailed Analysis", className="fw-bold")),

    dbc.CardBody([
        html.Label("Select companies:", className="fw-bold"),
        details_company_dropdown,

        html.Label("Select fuel types:", className="fw-bold"),
        fuel_types_dropdown,

        html.Label("Select car types:", className="fw-bold"),
        car_types_dropdown,

        html.Label("Select price range:", className="fw-bold"),
        html.Div(price_range_slider, style={"display": "none"}),
        html.Div([min_price_input, max_price_input], className="d-flex justify-content-between"),
        html.P(id="currency-label", className="text-muted text-end"),

        html.Label("Select total speed range:", className="fw-bold"),
        total_speed_range_slider,
        html.Div([min_total_speed_input, max_total_speed_input], className="d-flex justify-content-between", style={"display": "none !important"}),
        html.P("km/h", className="text-muted text-end"),

        html.Label("Select seat numbers:", className="fw-bold"),
        seats_range_slider,
        html.Div([min_seats_input, max_seats_input], className="d-flex justify-content-between", style={"display": "none !important"}),
        html.P("Seats", className="text-muted text-end"),
    ])
], body=True, className="p-3 h-100")

# DETAILED ANALYSIS - CHARTS
scatter_plot_card = dbc.Card([
    html.Div([
        html.H6(id="scatter-plot-title", className="fw-bold text-center mb-3"),
        dvc.Vega(id="scatter-plot", className="align-self-start ms-2"),
        dcc.RadioItems(
            id="scatter-toggle",
            options=[
                {"label": " Horsepower", "value": "horsepower"},
                {"label": " Performance", "value": "performance_0_100_km/h"},
                {"label": " Total speed", "value": "total_speed"},
            ],
            value="horsepower",
            inline=True,
            className="mt-2 d-flex justify-content-center",
            labelStyle={'margin-right': '15px', 'white-space': 'nowrap'}
        )
    ], className="d-flex flex-column justify-content-center align-items-center h-100")
], body=True, className="p-3 h-100")

price_boxplot_card = dbc.Card([
    html.Div([
        html.H6(id="price-boxplot-title", className="fw-bold text-center mb-3"),
        dvc.Vega(id="price-boxplot", className="align-self-start ms-2"),
        dcc.RadioItems(
            id="boxplot-category-radio1",
            options=[
                {"label": " Company", "value": "company_names"},
                {"label": " Fuel type", "value": "fuel_types_cleaned"},
            ],
            value="company_names", inline=True, className="mt-2 d-flex justify-content-center",
            labelStyle={'margin-right': '15px'}
        )
    ], className="d-flex flex-column justify-content-center align-items-center h-100")
], body=True, className="p-3 h-100")

horsepower_boxplot_card = dbc.Card([
    html.Div([
        html.H6(id="horsepower-boxplot-title", className="fw-bold text-center mb-3"),
        dvc.Vega(id="horsepower-boxplot", className="align-self-start ms-2"),
        dcc.RadioItems(
            id="boxplot-category-radio2",
            options=[
                {"label": " Company", "value": "company_names"},
                {"label": " Fuel type", "value": "fuel_types_cleaned"},
            ],
            value="company_names", inline=True, className="mt-2 d-flex justify-content-center",
            labelStyle={'margin-right': '15px'}
        )
    ], className="d-flex flex-column justify-content-center align-items-center h-100")
], body=True, className="p-3 h-100")

# FOOTER SECTION
footer = dbc.Container([
    html.Div([
        html.P([
            "VDash is a powerful dashboard designed for car buyers and automotive professionals, enabling easy comparison of vehicles!"
        ], className="text-center mb-1"),
        html.P([
            "Developed by Abeba Nigussie Turi, Alexandra Zhou, Archer Liu, and Essie Zhang | ",
            html.A("Car Data Source", href="https://www.kaggle.com/datasets/abdulmalik1518/the-ultimate-cars-dataset-2024", target="_blank"),
            " | ",
            html.A("View Source Code", href="https://github.com/UBC-MDS/DSCI-532_2025_4_vdash", target="_blank"),
            " | Last updated: {}".format(datetime.now().strftime('%B %d, %Y'))
        ], className="text-center")
    ])
], className="mt-4")

# MAIN LAYOUT
# app.layout = dbc.Container([
#     header,

#     # Company Overview Section
#     dbc.Row([
#         dbc.Col(company_overview, width=12)
#     ], className="mb-4"),

#     # Detailed Analysis Section (Filters & Charts)
#     dbc.Row([
#         dbc.Col(sidebar, width=3),
#         dbc.Col(scatter_plot_card, width=3),
#         dbc.Col(price_boxplot_card, width=3),
#         dbc.Col(horsepower_boxplot_card, width=3),
#     ], className="g-3"),

#     # Footer Section
#     footer

# ], fluid=True)

app.layout = dbc.Container([
    header,
    dcc.Tabs([
        dcc.Tab(label='About', children=[
            dbc.Card([
                dbc.CardBody([
                    html.H3("🚀 Happy car hunting with VDash!", className="fw-bold mb-4"),
                    html.P(
                        "Welcome to VDash, an interactive dashboard for car buyers and automotive professionals to compare vehicles! "
                        "Effortlessly compare vehicles based on performance, pricing, and key features with dynamic filters and interactive visuals.",
                        className="mb-4"
                    ),
                    html.H4("Motivation and Purposes", className="fw-bold mb-3"),
                    html.P(
                        "VDash is a user-friendly interactive vehicle comparison dashboard customized for buyers in Canada. "
                        "Choosing the right car can be overwhelming, and this dashboard simplifies the process by empowering users with data-driven insights. "
                        "It is designed to assist users in making informed vehicle purchasing decisions through dynamic data visualization and exploration of the market through visual aids. "
                        "The dashboard enables users to filter and compare cars based on multiple attributes such as price, horsepower, battery/engine capacity, speed, fuel type, seating capacity, and car type. "
                        "By providing an interactive experience, the dashboard allows users to visualize trends, compare specifications across different models, and identify the best options based on their preferences.",
                        className="mb-4"
                    ),
                    html.H4("Key Features", className="fw-bold mb-3"),
                    html.Ul([
                        html.Li("Compare Vehicles Across Multiple Attributes: Filter cars by price, horsepower, battery/engine capacity, speed, fuel type, seating capacity, and car type to find the best fit for your needs."),
                        html.Li("Visualize Market Trends: Use dynamic plots to understand pricing distributions, performance differences, and how various car models compare."),
                        html.Li("Make Data-Driven Decisions: Gain insights into key vehicle attributes with side-by-side comparisons and interactive visual analytics."),
                        html.Li("Customize Your Search: Adjust sliders and dropdowns to refine your car search quickly and effectively. Toggle between CAD & USD pricing to view costs in your preferred currency."),
                        html.Li("Enhance Your Car Buying Experience: Whether you’re a buyer, seller, or automotive enthusiast, VDash simplifies complex comparisons and helps you make informed purchasing decisions."),
                    ], className="mb-4"),
                ])
            ], className="p-3")
        ]),
        dcc.Tab(label='Company Overview', children=[
            dbc.Row([
                dbc.Col(company_sidebar, width=3),
                dbc.Col([
                    dbc.Row([
                        dbc.Col(bar_chart_card, width=6),
                        dbc.Col(histogram_card, width=6),
                    ], className="g-2 h-100")
                ], width=9)
            ], className="g-3 h-100")
        ]),
        dcc.Tab(label='Detailed Analysis', children=[
            dbc.Row([
                dbc.Col(sidebar, width=3),
                dbc.Col(scatter_plot_card, width=3),
                dbc.Col(price_boxplot_card, width=3),
                dbc.Col(horsepower_boxplot_card, width=3),
            ], className="g-3")
        ]),
    ]),
    footer
], fluid=True)


# Run the Dash app
if __name__ == '__main__':
    app.run(debug=False)  # Change to False for deployment
