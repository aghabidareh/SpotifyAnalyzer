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


@app.callback(
    [
        Output('scatter-plot', 'figure'),
        Output('histogram', 'figure'),
        Output('box-plot', 'figure'),
        Output('bar-plot', 'figure')
    ],
    [
        Input('genre-filter', 'value'),
        Input('popularity-slider', 'value'),
        Input('feature-dropdown', 'value')
    ]
)
def update_plots(selected_genres, popularity_range, selected_feature):
    filtered_data = data[
        (data['genre'].isin(selected_genres)) &
        (data['popularity'].between(popularity_range[0], popularity_range[1]))
        ]

    scatter_fig = px.scatter(
        filtered_data,
        x=selected_feature,
        y='popularity',
        color='genre',
        hover_data=['track_name', 'artist_name'],
        title=f'{selected_feature.capitalize()} vs Popularity'
    )
    scatter_fig.update_layout(transition_duration=500)

    hist_fig = px.histogram(
        filtered_data,
        x=selected_feature,
        color='genre',
        title=f'Distribution of {selected_feature.capitalize()}',
        nbins=30
    )
    hist_fig.update_layout(transition_duration=500)

    box_fig = px.box(
        filtered_data,
        x='genre',
        y=selected_feature,
        color='genre',
        title=f'{selected_feature.capitalize()} by Genre'
    )
    box_fig.update_layout(transition_duration=500)

    top_artists = filtered_data.groupby('artist_name')['popularity'].mean().sort_values(ascending=False).head(10)
    bar_fig = px.bar(
        x=top_artists.values,
        y=top_artists.index,
        orientation='h',
        title='Top 10 Artists by Average Popularity',
        labels={'x': 'Average Popularity', 'y': 'Artist'}
    )
    bar_fig.update_layout(transition_duration=500)

    return scatter_fig, hist_fig, box_fig, bar_fig


@app.callback(
    Output('track-details', 'children'),
    Input('scatter-plot', 'clickData'),
    State('genre-filter', 'value'),
    State('popularity-slider', 'value')
)
def display_track_details(clickData, selected_genres, popularity_range):
    if clickData is None:
        return "Click on a point in the scatter plot to see track details."

    point = clickData['points'][0]
    track_name = point['customdata'][0]
    artist_name = point['customdata'][1]

    track_data = data[
        (data['track_name'] == track_name) &
        (data['artist_name'] == artist_name) &
        (data['genre'].isin(selected_genres)) &
        (data['popularity'].between(popularity_range[0], popularity_range[1]))
        ]

    if not track_data.empty:
        track = track_data.iloc[0]
        details = [
            html.P(f"Track: {track['track_name']}"),
            html.P(f"Artist: {track['artist_name']}"),
            html.P(f"Genre: {track['genre']}"),
            html.P(f"Popularity: {track['popularity']}"),
            html.P(f"Danceability: {track['danceability']:.2f}"),
            html.P(f"Energy: {track['energy']:.2f}"),
            html.P(f"Valence: {track['valence']:.2f}")
        ]
        return details
    return "No details available for this track."
