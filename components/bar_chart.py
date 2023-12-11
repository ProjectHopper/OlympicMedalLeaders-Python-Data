from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc 
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("bar_chart", "children"),
            Input("dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = data.query('Team in @dropdown')
        if filtered_data.shape[0]==0:
            return html.Div(
                [
                dbc.Alert("No countries selected", color="danger"),
                ],
                id="bar_chart"
            )
        fig = px.bar(
            filtered_data,
            x="Medal",
            y="Count",
            color="Team",
            title="Medals by countries"
        )
        return html.Div(dcc.Graph(figure=fig),id="bar_chart")
    return html.Div(id="bar_chart")