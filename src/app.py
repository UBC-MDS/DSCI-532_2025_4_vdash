import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import src.callbacks  # Import all callbacks, DON'T REMOVE!
from src.components.structural_elements import (
    create_header,
    create_company_sidebar,
    create_detailed_sidebar,
    create_bar_chart_card,
    create_histogram_card,
    create_scatter_plot_card,
    create_price_boxplot_card,
    create_horsepower_boxplot_card,
    create_footer,
    create_about_tab
)

# Initialize Dash App with Bootstrap Theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# MAIN LAYOUT
app.layout = dbc.Container([
    create_header(),
    dcc.Tabs([
        dcc.Tab(label='Company Overview', children=[
            dbc.Row([
                dbc.Col(create_company_sidebar(), width=3),
                dbc.Col([
                    dbc.Row([
                        dbc.Col(create_bar_chart_card(), width=6),
                        dbc.Col(create_histogram_card(), width=6),
                    ], className="g-2 h-100")
                ], width=9)
            ], className="g-3 h-100")
        ]),
        dcc.Tab(label='Detailed Analysis', children=[
            dbc.Row([
                dbc.Col(create_detailed_sidebar(), width=3),
                dbc.Col(create_scatter_plot_card(), width=3),
                dbc.Col(create_price_boxplot_card(), width=3),
                dbc.Col(create_horsepower_boxplot_card(), width=3),
            ], className="g-3")
        ]),
        create_about_tab(),
    ]),
    create_footer()
], fluid=True)


# Run the Dash app
if __name__ == '__main__':
    app.run(debug=False)  # Change to False for deployment
