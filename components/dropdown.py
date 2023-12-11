from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc 

def render(app, data):
    list_countries = data["Team"].unique()
    all_countries = [{"label":c,"value":c} for c in list_countries]

    @app.callback(
            Output("dropdown","value"),
            Input("button", "n_clicks")
    )
    def update_all_countries(n):
        return list_countries
    
    return html.Div(
        [
            html.H6("Select countries"),
            dcc.Dropdown(
                options=all_countries,
                multi=True,
                value="United States",
                id = "dropdown"
            ),
            dbc.Button(
                children=["Select all"],
                color = "primary",
                n_clicks = 0,
                id = "button"
            )
        ]
    )