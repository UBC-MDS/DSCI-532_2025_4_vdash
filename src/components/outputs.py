import altair as alt
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


# ============ OUTPUTS ============

# Card: Max total speed & horsepower within selected companies
def max_speed_horsepower(df):
    if df.empty:
        return None, None

    max_speed = df['total_speed'].max()
    max_hp = df['horsepower'].max()

    return max_speed, max_hp


# Gauges: Max speed and horsepower gauges
def create_gauge_cards(max_speed, max_hp):
    # Speed gauge
    speed_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=max_speed,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': 'Max Speed (km/h)', 'font': {'size': 16, 'weight': 'bold'}},
        gauge={
            'axis': {
                'range': [None, 500],
                'tickmode': 'linear',
                'tick0': 0,
                'dtick': 100
            },
            'bar': {'color': "Navy"},
        },
        number={'font': {'size': 24}}
    ))
    speed_fig.update_layout(
        width=220,
        height=130,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='white',
        autosize=False
    )

    # Horsepower gauge
    hp_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=max_hp,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': 'Max Horsepower', 'font': {'size': 16, 'weight': 'bold'}},
        gauge={
            'axis': {
                'range': [None, 2500],
                'tickmode': 'linear',
                'tick0': 0,
                'dtick': 500
            },
            'bar': {'color': "FireBrick"},
        },
        number={'font': {'size': 24}}
    ))
    hp_fig.update_layout(
        width=220,
        height=130,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='white',
        autosize=False
    )

    return html.Div([
        dbc.Row([
            dbc.Col([
                html.Div(
                    dcc.Graph(
                        figure=speed_fig,
                        config={'displayModeBar': False}
                    ),
                    className="d-flex justify-content-center"
                )
            ], width=12, className="mb-2"),
            dbc.Col([
                html.Div(
                    dcc.Graph(
                        figure=hp_fig,
                        config={'displayModeBar': False}
                    ),
                    className="d-flex justify-content-center"
                )
            ], width=12)
        ])
    ], className="d-flex flex-column align-items-center")


# Bar chart: number of car models in each company
def plot_bar_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('count()', title='Number of Car Models'),
        y=alt.Y('company_names:N', title='Company'),
        color=alt.Color('company_names:N', legend=None),
        tooltip=[
            alt.Tooltip('company_names:N', title='Company'),
            alt.Tooltip('count()', title='Count')
        ]
    ).properties(
        width="container",
        height=400
    ).interactive().to_dict(format="vega")

    return chart


# Histogram: car price range histogram for selected company
def plot_grouped_histogram(df, price_col, currency='CAD'):
    if currency == 'CAD':
        price_bins = [0, 20000, 30000, 50000, 80000, 100000, float('inf')]
        price_labels = ["0-20K", "20-30K", "30-50K", "50-80K", "80-100K", "100K+"]
        x_title = "Price Range (CAD)"
    else:  # USD
        price_bins = [0, 15000, 22000, 37000, 60000, 75000, float('inf')]
        price_labels = ["0-15K", "15-22K", "22-37K", "37-60K", "60-75K", "75K+"]
        x_title = "Price Range (USD)"

    # Bin the price column into categories
    df = df.copy()
    df['Price Range'] = pd.cut(
        df[price_col],
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
        width="container",
        height=400
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
        .properties(width="container", height=400)
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
        width="container",
        height=400
    ).to_dict(format="vega")

    return price_boxplot


# Empty plot: shows when no data avaliable
def empty_warning_plot():
    return alt.Chart().mark_text(
        text="No data available",
        fontSize=14,
    ).properties(
        width=200, height=350
    ).to_dict()


# Boxplot: Horsepower distribution with category selection
def plot_boxplot_horsepower(df, category="company_names", price_col="cars_prices_cad", min_price=None, max_price=None):
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

    boxplot = alt.Chart(df).mark_boxplot().encode(
        x=alt.X(f"{category}:N",
                title=display_name,
                axis=alt.Axis(labelAngle=-360)),
        y=alt.Y("horsepower:Q",
                title="Horsepower"),
        color=alt.Color(f"{category}:N",
                        title=display_name,
                        legend=alt.Legend(title=display_name))
    )

    summary_df = df.groupby(category)['horsepower'].describe().reset_index()
    summary_df = summary_df.rename(columns={"25%": "Q1", "50%": "Median", "75%": "Q3"})

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

    horsepower_boxplot = alt.layer(boxplot, whisker).properties(
        width="container",
        height=400
    ).to_dict(format="vega")

    return horsepower_boxplot
