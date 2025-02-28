from dash import Input, Output, callback, html
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data import cars_df
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
    max_seats_input,
    max_speed_horsepower,
    plot_bar_chart,
    plot_grouped_histogram
)


all_companies = sorted(cars_df['company_names'].unique())
min_price_cad = cars_df['cars_prices_cad'].min()  # 5,400
max_price_cad = cars_df['cars_prices_cad'].max()  # 24,300,000
min_price_usd = cars_df['cars_prices_usd'].min()  # 4,000
max_price_usd = cars_df['cars_prices_usd'].max()  # 18,000,000


# Callback to update currency state
@callback(
    [Output('currency-cad-btn', 'className'),
     Output('currency-usd-btn', 'className')],
    [Input('currency-cad-btn', 'n_clicks'),
     Input('currency-usd-btn', 'n_clicks')]
)
def update_currency_buttons(cad_clicks, usd_clicks):
    cad_clicks = cad_clicks or 0
    usd_clicks = usd_clicks or 0

    if cad_clicks == 0 and usd_clicks == 0:
        return "active-btn", "inactive-btn"

    if cad_clicks >= usd_clicks and usd_clicks == 0:
        return "active-btn", "inactive-btn"
    elif usd_clicks >= cad_clicks and cad_clicks == 0:
        return "inactive-btn", "active-btn"
    elif cad_clicks > usd_clicks:
        return "active-btn", "inactive-btn"
    else:
        return "inactive-btn", "active-btn"


# Callback to synchronize sliders and input boxes
@callback(
    [Output('min-price-input', 'value', allow_duplicate=True),
     Output('max-price-input', 'value', allow_duplicate=True)],
    [Input('price-range-slider', 'value')],
    prevent_initial_call=True
)
def sync_price_inputs(slider_value):
    min_price, max_price = slider_value
    return min_price, max_price


@callback(
    Output('price-range-slider', 'value', allow_duplicate=True),
    [Input('min-price-input', 'value'),
     Input('max-price-input', 'value')],
    prevent_initial_call=True
)
def sync_price_slider(min_input, max_input):
    return [min_input, max_input]


@callback(
    [Output('min-price-input', 'value', allow_duplicate=True),
     Output('max-price-input', 'value', allow_duplicate=True),
     Output('price-range-slider', 'min'),
     Output('price-range-slider', 'max'),
     Output('price-range-slider', 'value', allow_duplicate=True)],
    [Input('currency-cad-btn', 'className'),
     Input('currency-usd-btn', 'className')],
    prevent_initial_call=True
)
def update_price_components(cad_class, usd_class):
    if cad_class == "active-btn":
        return min_price_cad, max_price_cad, min_price_cad, max_price_cad, [min_price_cad, max_price_cad]
    else:
        return min_price_usd, max_price_usd, min_price_usd, max_price_usd, [min_price_usd, max_price_usd]


@callback(
    [Output('min-total-speed-input', 'value'),
     Output('max-total-speed-input', 'value')],
    [Input('total-speed-range-slider', 'value')]
)
def sync_speed_inputs(slider_value):
    min_speed, max_speed = slider_value
    return min_speed, max_speed


@callback(
    Output('total-speed-range-slider', 'value'),
    [Input('min-total-speed-input', 'value'),
     Input('max-total-speed-input', 'value')]
)
def sync_speed_slider(min_input, max_input):
    return [min_input, max_input]


@callback(
    [Output('min-seats-input', 'value'),
     Output('max-seats-input', 'value')],
    [Input('seats-range-slider', 'value')]
)
def sync_seats_inputs(slider_value):
    min_seats, max_seats = slider_value
    return min_seats, max_seats


@callback(
    Output('seats-range-slider', 'value'),
    [Input('min-seats-input', 'value'),
     Input('max-seats-input', 'value')]
)
def sync_seats_slider(min_input, max_input):
    return [min_input, max_input]


# Company dropdown limit selection to 5
@callback(
    Output('overview-company-dropdown', 'options'),
    Input('overview-company-dropdown', 'value')
)
def limit_overview_dropdown_options(selected_companies):
    if len(selected_companies) >= 5:
        return [{'label': company, 'value': company, 'disabled': company not in selected_companies} for company in all_companies]
    return [{'label': company, 'value': company} for company in all_companies]


@callback(
    Output('details-company-dropdown', 'options'),
    Input('details-company-dropdown', 'value')
)
def limit_details_dropdown_options(selected_companies):
    if len(selected_companies) >= 5:
        return [{'label': company, 'value': company, 'disabled': company not in selected_companies} for company in all_companies]
    return [{'label': company, 'value': company} for company in all_companies]


@callback(
    Output("max-speed-hp-card", "children"),
    Input("overview-company-dropdown", "value")
)
def update_speed_hp_card(selected_companies):
    if not selected_companies:
        return "Select at least one company to view max speed & horsepower."

    filtered_df = cars_df[cars_df['company_names'].isin(selected_companies)]
    max_speed, max_hp = max_speed_horsepower(filtered_df)

    if max_speed is None or max_hp is None:
        return "No data available for selected companies."

    return html.Div([
        html.H3(f"{max_speed} KM/H"),
        html.P("Max total speed"),
        html.H3(f"{max_hp} HP"),
        html.P("Max horsepower")
    ])


@callback(
    Output('cars-bar-chart', 'spec'),
    Input('overview-company-dropdown', 'value')
)
def update_bar_chart(selected_companies):
    if not selected_companies:
        return {}
    filtered_df = cars_df[cars_df['company_names'].isin(selected_companies)]
    return plot_bar_chart(filtered_df)


@callback(
    Output('price-range-histogram', 'spec'),
    [Input('overview-company-dropdown', 'value'),
     Input('currency-cad-btn', 'className')]
)
def update_histogram(selected_companies, cad_class):
    if not selected_companies:
        return {}
    currency = 'CAD' if cad_class == "active-btn" else 'USD'
    filtered_df = cars_df[cars_df['company_names'].isin(selected_companies)]
    return plot_grouped_histogram(filtered_df, currency)
