import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/")

# Dane
# 1. Słownik danych
places_dict = {
    "Miejsce": [
        "Hotel",
        "Park",
        "Muzem",
        "Wieżowce",
        "Broadway",
        "Stadion",
        "Zwiedzanie",
        "Budynki",
        "Budynki",
        "Zwiedzanie",
        "Park",
        "Zakupy",
        "Pub",
        "Budynki",
        "Budynki",
        "Budynki",
        "Muzem",
        "Muzem",
        "Zwiedzanie",
        "Budynki",
        "Zwiedzanie",
        "Zakupy",
        "Zwiedzanie",
        "Muzem",
        "Zakupy",
        "Zakupy",
        "Zakupy",
        "Muzem",
        "Zwiedzanie",
    ],
    "Nazwa": [
        "Best Western Plus Meadowlands",
        "Central Park",
        "Muzeum Guggenheima w Nowym Jorku",
        "Rockefeller Center",
        "Gershwin Theatre",
        "Yankee Stadium",
        "Times Square",
        "Arconia",
        "DUMBO Manhattan Bridge View",
        "Pebble Beach",
        "Brooklyn Bridge Park",
        "Harry Potter Shop New York",
        "McGee's Pub",
        "Friends Apartment Building",
        "How I Met Your Mother Address",
        "Grand Central Terminal",
        "Metropolitan Museum of Art",
        "Amerykańskie Muzeum Historii Naturalnej",
        "New York City Elevated View Point",
        "Edge",
        "High Line Boardwalk",
        "The LEGO® Store Fifth Avenue",
        "Katedra św, Patryka w Nowym Jorku",
        "Madame Tussauds New York",
        "Midtown Comics Times Square",
        "Microsoft Experience Center",
        "Apple Fifth Avenue",
        "Museum of the City of New York",
        "Nowojorska Biblioteka Publiczna",
    ],
    "Adres": [
        "250 Harmon Meadow Blvd, Secaucus, NJ 07094, Stany Zjednoczone",
        "Nowy Jork, 10024, Stany Zjednoczone",
        "1071 5th Ave, New York, NY 10128, Stany Zjednoczone",
        "45 Rockefeller Plaza, New York, NY 10111, Stany Zjednoczone",
        "222 W 51st St, New York, NY 10019, Stany Zjednoczone",
        "1 E 161st St, Bronx, NY 10451, Stany Zjednoczone",
        "Manhattan, NY 10036, Stany Zjednoczone",
        "225 W 86th St, New York, NY 10024, Stany Zjednoczone",
        "39-21 Washington St, Brooklyn, NY 11201, Stany Zjednoczone",
        "65 Plymouth St, Brooklyn, NY 11201, Stany Zjednoczone",
        "Brooklyn, NY 11201, Stany Zjednoczone",
        "935 Broadway, New York, NY 10010, Stany Zjednoczone",
        "240 W 55th St, New York, NY 10019, Stany Zjednoczone",
        "90 Bedford St, New York, NY 10014, Stany Zjednoczone",
        "150 W 85th St, New York, NY 10024, Stany Zjednoczone",
        "89 E 42nd St, New York, NY 10017, Stany Zjednoczone",
        "1000 5th Ave, New York, NY 10028, Stany Zjednoczone",
        "200 Central Park W, New York, NY 10024, Stany Zjednoczone",
        "80 Furman St, Brooklyn, NY 11201, Stany Zjednoczone",
        "30 Hudson Yards, New York, NY 10001, Stany Zjednoczone",
        "New York, NY 10001, Stany Zjednoczone",
        "636 5th Ave, New York, NY 10020, Stany Zjednoczone",
        "5th Ave, New York, NY 10022, Stany Zjednoczone",
        "234 W 42nd St, New York, NY 10036, Stany Zjednoczone",
        "200 W 40th St, New York, NY 10018, Stany Zjednoczone",
        "677 5th Ave, New York, NY 10022, Stany Zjednoczone",
        "767 5th Ave, New York, NY 10153, Stany Zjednoczone",
        "1220 5th Ave, New York, NY 10029, Stany Zjednoczone",
        "476 5th Ave, New York, NY 10018, Stany Zjednoczone",
    ],
    "Geo sz": [
        40.78880504, 40.77809036, 40.78351222, 40.75882932, 40.76253447, 40.82991008,
        40.75845738, 40.78840478, 40.70342265, 40.70445055, 40.70248898, 40.74070169,
        40.7649267, 40.73245909, 40.78669468, 40.75343213, 40.77949886, 40.78157265,
        40.70143622, 40.7534992, 40.7564494, 40.75931523, 40.75872542, 40.75660208,
        40.75491925, 40.7605476, 40.76387493, 40.79255479, 40.75327164
    ],
    "Geo dł": [
        -74.04619913, -73.96910531, -73.95908895, -73.9786577, -73.98537748, -73.92634846,
        -73.98554076, -73.97548693, -73.989573, -73.99002153, -73.99579577, -73.98964839,
        -73.98301689, -74.00530764, -73.9745146, -73.97680144, -73.96328753, -73.9739692,
        -73.99595322, -74.00104427, -74.00357622, -73.97713795, -73.97621675, -73.9882901,
        -73.98838858, -73.97534343, -73.97298007, -73.95198053, -73.98228558
    ]
}
# Sprawdzamy długości kolumn
# for k, v in places_dict.items():
#     print(k, len(v))
# 2. Tworzymy DataFrame
places = pd.DataFrame(places_dict)
# Tworzymy mapę
fig = px.scatter_mapbox(
    places,
    lat="Geo sz",
    lon="Geo dł",
    hover_name="Nazwa",
    zoom=10,
    #  symbol="Miejsce",  # różne kategorie mają różne symbole
     color="Miejsce",   # kolory wg kategorii
    
)
# fig.update_layout(mapbox_style="open-street-map")

fig.update_layout(
    mapbox_style="open-street-map",
    autosize=True,
    margin={"r":0,"t":0,"l":0,"b":0},  # usuwa marginesy
)

# Layout strony
layout = html.Div([
    html.H2("Mapa miejsc"),
    dcc.Graph(
    id="mapa",
    figure=fig,
    style={
        "width": "100%",    # zajmuje całą szerokość
        "height": "65vh",   # 80% wysokości okna przeglądarki
        "margin": "0 auto"  # wyśrodkowanie
    },
    config={"displayModeBar": False}  # opcjonalnie pasek narzędzi
),

    # # html.H2("Tabela miejsc"),
    # dash_table.DataTable(
    #     id="tabela",
    #     columns=[{"name": i, "id": i} for i in places.columns],
    #     data=places.to_dict("records"),
    #     page_size=5,
    #     style_table={"overflowX": "auto"}
    # )
])
