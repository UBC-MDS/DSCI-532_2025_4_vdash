import sys
import os
import pandas as pd
import altair as alt
from dash import Dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_vega_components as dvc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
<<<<<<< HEAD
=======
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import src.callbacks
>>>>>>> d65e912a28f4befb8c64ca9a10148055038c5d89
from src.components import (
    currency_switch_btns,
    overview_company_dropdown,
    details_company_dropdown,
    fuel_types_dropdown,
    # car_types_dropdown,
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

from src.data import cars_df 

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
        html.Div(id="max-speed-hp-card"),  # Max total speed & horsepower
        dvc.Vega(id='cars-bar-chart'),  # Bar chart
        dvc.Vega(id='price-range-histogram')  # Grouped histogram
    ], className='company-overview'),

    # Section 2: Detailed Analysis
    html.Div([
        html.H2("Detailed Analysis"),

        # Filters
        details_company_dropdown,
        fuel_types_dropdown,
        # car_types_dropdown,
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

        # Scatterplot Attribute Selector
        html.Label("Select attribute to compare against Price:"),
        dcc.RadioItems(
        id="x-axis-selector",
        options=[
            {"label": "Horsepower", "value": "Horsepower"},
            {"label": "Performance", "value": "Performance"},
            {"label": "Total Speed", "value": "Total Speed"}
        ],
        value="horsepower",
        inline=True  # Display as horizontal buttons
    ),

        

        # Visuals
        html.Div(
            id="scatter-plot", 
            className='chart-placeholder'
        ),
        # html.Div(
        #     "Placeholder for Car Price Boxplot",
        #     className='chart-placeholder'
        # ),
        html.Div([
            dcc.RadioItems(
                id='boxplot-category-radio1',
                options=[
                    {'label': 'Company', 'value': 'company_names'},
                    # {'label': 'Car type', 'value': 'car_types'},
                    {'label': 'Fuel type', 'value': 'fuel_types_cleaned'}
                ],
                value='company_names',
                labelStyle={'display': 'inline-block', 'margin-right': '10px'}
            ),
            dvc.Vega(id='price-boxplot')
        ]),
        # html.Div(
        #     "Placeholder for Horsepower Boxplot",
        #     className='chart-placeholder'
        # ),
        html.Div([
            dcc.RadioItems(
                id='boxplot-category-radio2',
                options=[
                    {'label': 'Company', 'value': 'company_names'},
                    # {'label': 'Car type', 'value': 'car_types'},
                    {'label': 'Fuel type', 'value': 'fuel_types_cleaned'}
                ],
                value='company_names',
                labelStyle={'display': 'inline-block', 'margin-right': '10px'}
            ),
            dvc.Vega(id='horsepower-boxplot') # Horsepower boxplot
        ])

    ], className='detailed-analysis'),
])

def horsepower_price(filtered_df, x_var, price_col):
    chart = (
        alt.Chart(filtered_df)
        .mark_circle(size=80, opacity=0.8)
        .encode(
            x=alt.X(x_var, title= "Horse Power"),
            y=alt.Y(price_col, title="Price"),
            color=alt.Color("company_names", legend=alt.Legend(title="Company")),
            tooltip=["cars_names", "fuel_types_cleaned", price_col]
        )
        .properties(width=500, height=400)
        .interactive()
    )

    return chart


# app callbacks
@app.callback(
    Output("scatter-plot", "children"),
    [
        Input("details-company-dropdown", "value"),  
        Input("fuel-types-dropdown", "value"),  
        Input("price-range-slider", "value"),  
        Input("total-speed-range-slider", "value"),  
        Input("seats-range-slider", "value"),  
        Input("x-axis-selector", "value"),
        Input("currency-cad-btn", "n_clicks"),  # Track CAD button clicks
        Input("currency-usd-btn", "n_clicks"),  # Track USD button clicks
    ]
)
def update_scatter_plot(selected_companies, selected_fuels, price_range, speed_range, seat_range, x_var, cad_clicks, usd_clicks):
    cad_clicks = cad_clicks or 0
    usd_clicks = usd_clicks or 0
    
    if cad_clicks > usd_clicks:
        price_col = "cars_prices_cad"
    else:
        price_col = "cars_prices_usd"  # Default to USD if no selection

    print(f"Using column: {price_col}")
    
    # Apply filters
    filtered_df = cars_df[
        (cars_df[price_col] >= price_range[0]) & (cars_df[price_col] <= price_range[1]) &
        (cars_df["total_speed"] >= speed_range[0]) & (cars_df["total_speed"] <= speed_range[1]) &
        (cars_df["seats"] >= seat_range[0]) & (cars_df["seats"] <= seat_range[1])
    ]
    
    if selected_companies:
        filtered_df = filtered_df[filtered_df["company_names"].isin(selected_companies)]
    
    if selected_fuels:
        filtered_df = filtered_df[filtered_df["fuel_types_cleaned"].isin(selected_fuels)]

    # Generate Altair scatterplot
    scatter_chart = horsepower_price(filtered_df, x_var, price_col)

    # Convert Altair JSON to a Dash-compatible format
    return dvc.Vega(spec=scatter_chart.to_dict()) 


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)  # Set to False before deployment
