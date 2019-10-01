import config
import flask
import dash
import dash_ui as dui
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask_caching import Cache

import plotly.graph_objs as go



import pandas as pd

messier_catalog = pd.read_pickle(config.PIKLE_FILE)
messier_catalog["Type"] = messier_catalog["Type"].astype(str)

app = dash.Dash('Catalogue de messier', external_stylesheets=[dbc.themes.BOOTSTRAP])
cache = Cache(app.server, config={'CACHE_TYPE': 'null'})



text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)



@app.server.route('{}<image_path>'.format(config.static_endpoint))
def serve_image(image_path):
    image_name = '{}'.format(image_path)
    return flask.send_from_directory("../assets/", image_name)

def get_picture(messier_object="M42"):
    picture = go.Figure()

    y_min = -90
    y_max = 90


    picture.update_layout(
        images=[
            go.layout.Image(
                source=config.static_url + messier_object +".jpg",
                xref="x",
                yref="y",
                x=0,
                y=y_max,
                sizex=24,
                sizey=y_max-y_min,
                sizing="contain",
                opacity=1,
                layer="above")
        ]
    )
    picture.update_layout(
        autosize=False,
        width=900,
        height=900)

    picture.update_xaxes(range=[0, 24])
    picture.update_yaxes(range=[y_min, y_max])
    return picture

def get_sky_map(_opacity=3):
    sky_map = go.Figure()

    colors = ["#001f3f", "#0074d9", "#3d9970", "#111111", "#01ff70", "#ffdc00", "#ff851B", "#ff4136", "#85144b", "#f012be", "#b10dc9", "#AAAAAA", "#111111"]
    for ind, type_object in enumerate(messier_catalog["Type"].unique().tolist()):
        filtered_data = messier_catalog[messier_catalog["Type"] == type_object]

        sky_map.add_trace(
            go.Scatter(
                x=24 - filtered_data["RA_h"],
                y=filtered_data["DEC_deg"],
                text=filtered_data["M#"] ,
                name=type_object,
                opacity=1,
                mode="markers",
                marker={
                    'size': 5,
                    'line': {"width": 1},
                    'color': colors[ind]
                }
            )
        )


    y_min = -90
    y_max = 90


    sky_map.update_layout(
        images=[
            go.layout.Image(
                source=config.static_url + "starMap.png",
                xref="x",
                yref="y",
                x=0,
                y=y_max,
                sizex=24,
                sizey=y_max-y_min,
                sizing="stretch",
                opacity=_opacity/10,
                layer="below")
        ]
    )
    sky_map.update_layout(
        autosize=False,
        width=1700,
        height=900)

    sky_map.update_xaxes(range=[0, 24])
    sky_map.update_yaxes(range=[y_min, y_max])
    return sky_map

def get_discover_timeline():
    discover_timeline = go.Figure()

    colors = ["#001f3f", "#0074d9", "#3d9970", "#111111", "#01ff70", "#ffdc00", "#ff851B", "#ff4136", "#85144b", "#f012be", "#b10dc9", "#AAAAAA", "#111111"]

    decouvreurs = messier_catalog.groupby("Decouvreur")["Date_decouverte"].mean().sort_values(ascending=True).reset_index()["Decouvreur"].tolist()


    for ind, decouvreur in enumerate(decouvreurs):
        filtered_data = messier_catalog[messier_catalog["Decouvreur"] == decouvreur]

        discover_timeline .add_trace(
            go.Scatter(
                x=filtered_data["Date_decouverte"],
                y= [ind] * len(filtered_data),
                text=filtered_data["M#"] ,
                name=f"{decouvreur} ({len(filtered_data)})",
                opacity=1,
                mode="markers",
                marker={
                    'size': 5,
                    'line': {"width": 1},
                    'color': colors[ind % len(colors)]
                }
            )
        )



    return discover_timeline

def get_discover_per_magnitude():
    discover_per_magnitude = go.Figure()

    colors = ["#001f3f", "#0074d9", "#3d9970", "#111111", "#01ff70", "#ffdc00", "#ff851B", "#ff4136", "#85144b", "#f012be", "#b10dc9", "#AAAAAA", "#111111"]
    for ind, type_object in enumerate(messier_catalog["Type"].unique().tolist()):
        filtered_data = messier_catalog[messier_catalog["Type"] == type_object]

        discover_per_magnitude.add_trace(
            go.Scatter(
                x=filtered_data["Date_decouverte"],
                y=filtered_data["Aparent_Magnitude"],
                text=filtered_data["M#"] ,
                name=type_object,
                opacity=1,
                mode="markers",
                marker={
                    'size': 5,
                    'line': {"width": 1},
                    'color': colors[ind]
                }
            )
        )



    return discover_per_magnitude


app.layout = html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(id="image_place_holder", figure=get_picture()), align="center"),
            dbc.Col([
                dcc.Graph(id='sky_map', figure=get_sky_map()),
                dcc.Slider(id='slider_opacity', min=0,max=10,marks={i: f"{i*10}%" for i in range(11)}, value=3)
                ]),
        ]),


        dbc.Row([
            dbc.Col(dcc.Graph(id='discover_timeline', figure=get_discover_timeline())),
            dbc.Col(dcc.Graph(id='discover_per_magnitude', figure=get_discover_per_magnitude()))
        ]),
    ])


@app.callback(
    Output(component_id='sky_map', component_property='figure'),
    [Input(component_id='slider_opacity', component_property='value')]
)
def set_opacity(_opacity):
    return get_sky_map(_opacity)


@app.callback(
    Output(component_id='image_place_holder', component_property='figure'),
    [Input(component_id='sky_map', component_property='clickData'),
     Input(component_id='discover_timeline', component_property='clickData'),
     Input(component_id='discover_per_magnitude', component_property='clickData')
     ]
)
def set_picture(_clickdata1, _clickdata2, _clickdata3):
    if not _clickdata1 is None:
        _clickdata = _clickdata1
    if not _clickdata2 is None:
        _clickdata = _clickdata2
    if not _clickdata3 is None:
        _clickdata = _clickdata3
    try:
        return get_picture(_clickdata["points"][0]['text'])
    except:
        return get_picture()



app.server.run(config.host, config.port)

