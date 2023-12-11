from dash import html, dcc
import dash_bootstrap_components as dbc
from components import dropdown, bar_chart

def create_layout(app, data):
    return dbc.Container(
        [
            dbc.Row(
            dbc.Col(
                html.Div(html.H1("Olympic Medal Leaders by Country")),
                width={"size": 11, "offset": 3},
            )
        ),
        dbc.Row([
                dbc.Col(dropdown.render(app,data),lg=4),
                dbc.Col(bar_chart.render(app,data),lg=8),
                ]
                )
        ]
    )