from dash import Dash, html

# Initiatlize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("VDash: Speed Up Your Car Hunt"),
        html.Div("CAD/USD Switcher Placeholder", className='currency-switcher')
    ], className='header'),

    html.Div([
        html.H2("Company Overview"),
        html.Div("Placeholder for Company Multi-Selector", className='multi-selector'),
        html.Div("Placeholder for Summary Card", className='summary-card'),
        html.Div(
            "Placeholder for Number of Car Models in Each Company Bar Chart",
            className='chart-placeholder'
        ),
        html.Div(
            "Placeholder for Car Price Range Histogram for Selected Company",
            className='chart-placeholder'
        )
    ], className='company-overview')
])

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
