import dash
from dash import html, dcc
import os

# Tworzymy aplikację
app = dash.Dash(__name__, use_pages=True)
server = app.server  # <- ważne dla deployu

app.layout = html.Div([
    html.H1("Moja aplikacja Dash", style={"textAlign": "center"}),

    html.Div([
        dcc.Link(page["name"] + " | ", href=page["relative_path"])
        for page in dash.page_registry.values()
    ]),

    dash.page_container
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))