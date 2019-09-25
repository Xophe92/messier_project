import config
import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.graph_objs as go



import pandas as pd

messier_catalog = pd.read_pickle(config.PIKLE_FILE)
messier_catalog["Type"] = messier_catalog["Type"].astype(str)

app = dash.Dash('Catalogue de messier')

text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)

plotly_figure = go.Figure()

colors = ["#001f3f", "#0074d9", "#3d9970", "#111111", "#01ff70", "#ffdc00", "#ff851B", "#ff4136", "#85144b", "#f012be", "#b10dc9", "#AAAAAA", "#111111"]
for ind, type_object in enumerate(messier_catalog["Type"].unique().tolist()):
    filtered_data = messier_catalog[messier_catalog["Type"] == type_object]

    plotly_figure.add_trace(
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

print(config.static_url)

plotly_figure.update_layout(
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
            opacity=0.3,
            layer="below")
    ]
)
plotly_figure.update_layout(
    autosize=False,
    width=1700,
    height=900)

plotly_figure.update_xaxes(range=[0, 24])
plotly_figure.update_yaxes(range=[y_min, y_max])


static_image_route = config.static_endpoint
@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}.png'.format(image_path)
    return flask.send_from_directory("../assets/", image_name)

app.layout = html.Div([
        html.H2('My First Dash App', style=text_style),
        html.P('Enter a Plotly trace type into the text box, such as histogram, bar, or scatter.', style=text_style),
        dcc.Input(id='text1', placeholder='box', value=''),
        dcc.Graph(id='plot1', figure=plotly_figure),
    ])


app.server.run(config.host, config.port)
