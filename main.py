import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

data = pd.read_csv('data.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


