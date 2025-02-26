import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dash import Dash, html
from src.components import (
    currency_switch_btns,
    overview_company_dropdown,
    details_company_dropdown,
    fuel_types_dropdown,
    price_range_slider,
    min_price_input,
    max_price_input,
    total_speed_range_slider,
    min_total_speed_input,
    max_total_speed_input,
    seats_range_slider,
    min_seats_input,
    max_seats_input
)

# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("VDash: Speed Up Your Car Hunt"),
        currency_switch_btns
    ], className='header'),

    # Section 1: Company Overview
    html.Div([
        html.H2("Company Overview"),

        # Filters
        overview_company_dropdown,

        # Visuals
        html.Div("Placeholder for Summary Card", className='summary-card'),
        html.Div(
            "Placeholder for Number of Car Models in Each Company Bar Chart",
            className='chart-placeholder'
        ),
        html.Div(
            "Placeholder for Car Price Range Histogram for Selected Company",
            className='chart-placeholder'
        )
    ], className='company-overview'),

    # Section 2: Detailed Analysis
    html.Div([
        html.H2("Detailed Analysis"),

        # Filters
        details_company_dropdown,
        fuel_types_dropdown,
        html.Div([
            price_range_slider,
            html.Div([
                min_price_input,
                max_price_input
            ], className='input-boxes')
        ]),
        html.Div([
            total_speed_range_slider,
            html.Div([
                min_total_speed_input,
                max_total_speed_input
            ], className='input-boxes')
        ]),
        html.Div([
            seats_range_slider,
            html.Div([
                min_seats_input,
                max_seats_input
            ], className='input-boxes')
        ]),

        # Visuals
        html.Div(
            "Placeholder for Horsepower vs. Price Scatter Plot",
            className='chart-placeholder'
        ),
        html.Div(
            "Placeholder for Car Price Boxplot",
            className='chart-placeholder'
        ),
        html.Div(
            "Placeholder for Horsepower Boxplot",
            className='chart-placeholder'
        )
    ], className='detailed-analysis'),
])

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)  # Set to False before deployment
    # server = app.server  # Uncomment this line for deployment
