import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

data = pd.read_csv('data.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Spotify Analyzer Dashboard", className="text-center my-4", style={'color': '#1DB954'}),

    dbc.Row([
        dbc.Col([
            html.Label("Select Genres"),
            dcc.Dropdown(
                id='genre-filter',
                options=[{'label': genre, 'value': genre} for genre in sorted(data['genre'].unique())],
                value=data['genre'].unique()[:5].tolist(),  # Default: top 5 genres
                multi=True,
                style={'width': '100%'}
            )
        ], md=4),
        dbc.Col([
            html.Label("Popularity Range"),
            dcc.RangeSlider(
                id='popularity-slider',
                min=0,
                max=100,
                step=1,
                value=[0, 100],
                marks={i: str(i) for i in range(0, 101, 20)},
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ], md=4),
        dbc.Col([
            html.Label("Select Feature for Analysis"),
            dcc.Dropdown(
                id='feature-dropdown',
                options=[
                    {'label': 'Danceability', 'value': 'danceability'},
                    {'label': 'Energy', 'value': 'energy'},
                    {'label': 'Valence', 'value': 'valence'},
                    {'label': 'Loudness', 'value': 'loudness'},
                    {'label': 'Tempo', 'value': 'tempo'},
                    {'label': 'Acousticness', 'value': 'acousticness'},
                    {'label': 'Speechiness', 'value': 'speechiness'},
                    {'label': 'Instrumentalness', 'value': 'instrumentalness'},
                    {'label': 'Liveness', 'value': 'liveness'}
                ],
                value='danceability',
                style={'width': '100%'}
            )
        ], md=4)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.H3("Scatter Plot: Feature vs Popularity"),
            dcc.Graph(id='scatter-plot')
        ], md=6),
        dbc.Col([
            html.H3("Histogram of Selected Feature"),
            dcc.Graph(id='histogram')
        ], md=6)
    ]),

    dbc.Row([
        dbc.Col([
            html.H3("Box Plot by Genre"),
            dcc.Graph(id='box-plot')
        ], md=6),
        dbc.Col([
            html.H3("Top Artists by Popularity"),
            dcc.Graph(id='bar-plot')
        ], md=6)
    ]),

    dbc.Row([
        dbc.Col([
            html.H3("Track Details"),
            html.Div(id='track-details', style={'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
        ], md=12)
    ], className="mt-4"),

    dbc.Row([
        dbc.Col([
            dbc.Button("Download Filtered Data", id='download-btn', color='primary', className='mt-3'),
            dcc.Download(id='download-data')
        ], md=12)
    ])
], fluid=True)
