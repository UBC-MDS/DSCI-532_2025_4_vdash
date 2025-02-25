from dash import Dash, html

# Initiatlize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("VDash: Speed Up Your Car Hunt"),
        html.Div("CAD/USD Switcher Placeholder", className='currency-switcher')
    ], className='header'),

    # Section 1: Company Overview
    html.Div([
        html.H2("Company Overview"),

        # Filters
        html.Div("Placeholder for Company Multi-Selector", className='multi-selector'),

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
        html.Div("Placeholder for Company Multi-Selector", className='multi-selector'),
        html.Div("Placeholder for Fuel Type Selector", className='multi-selector'),
        html.Div("Placeholder for Price Range Slider", className='slider'),
        html.Div("Placeholder for Total Speed Range Slider", className='slider'),
        html.Div("Placeholder for Seat Number Slider", className='slider'),

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
    app.run(debug=False)
    server = app.server
