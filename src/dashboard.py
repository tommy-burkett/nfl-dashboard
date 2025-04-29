# Imports
from dash import Dash, dcc, html, Input, Output, callback

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the data from data/cleaned_data/ directory
df = pd.read_csv('data/cleaned_data/2020-2024_combined_nfl_data.csv')

# Get the unique years to use as buttons
all_years = df["Year"].unique()
all_years.sort()

# Create team colors dictionary
# https://www.eggradients.com/blog/nfl-team-colors
team_colors = {
    "Arizona Cardinals": "#97233F",
    "Atlanta Falcons": "#A71930",
    "Baltimore Ravens": "#241773",
    "Buffalo Bills": "#00338D",
    "Carolina Panthers": "#0085CA",
    "Chicago Bears": "#0B162A",
    "Cincinnati Bengals": "#FB4F14",
    "Cleveland Browns": "#FF3C00",
    "Dallas Cowboys": "#003594",
    "Denver Broncos": "#002244",
    "Detroit Lions": "#0076B6",
    "Green Bay Packers": "#203731",
    "Houston Texans": "#03202F",
    "Indianapolis Colts": "#002C5F",
    "Jacksonville Jaguars": "#006778",
    "Kansas City Chiefs": "#E31837",
    "Las Vegas Raiders": "#000000",
    "Los Angeles Chargers": "#0080C6",
    "Los Angeles Rams": "#003594",
    "Miami Dolphins": "#008E97",
    "Minnesota Vikings": "#4F2683",
    "New England Patriots": "#002244",
    "New Orleans Saints": "#D3BC8D",
    "New York Giants": "#0B2265",
    "New York Jets": "#125740",
    "Philadelphia Eagles": "#004C54",
    "Pittsburgh Steelers": "#FFB612",
    "San Francisco 49ers": "#AA0000",
    "Seattle Seahawks": "#69BE28",
    "Tampa Bay Buccaneers": "#D50A0A",
    "Tennessee Titans": "#4B92DB",
    "Washington Commanders": "#773141",
}

# Initialize the Dash app
def run_app() -> None:
    app = Dash(__name__)
    app.title = "NFL Dashboard"
    create_layout(app)
    app.run(debug=True)
    return None

# Create the layout for the app
def create_layout(app: Dash) -> None:

    # Create the layout
    app.layout = html.Div([
        html.H1("NFL Dashboard", 
                style={'textAlign': 'center',
                       'fontSize': '40px',
                       'margin': '20px 0'
                       }),

        html.Label("Select Side of the Ball (Offense/Defense):"),
        dcc.Dropdown(
            id='side-dropdown',
            options=[
                {'label': 'Offense', 'value': 'Offense'},
                {'label': 'Defense', 'value': 'Defense'}
            ],
            value='Offense',
            clearable=False,
            style={'width': '150px', 
                   'padding': '0 10px'
                   }
            ),
        

        # Add a break in the page for spacing
        html.Br(),

        # Format the graphs
        html.Div([
            # First graph
            html.Div([
                html.H3("Title"),
                html.Div([
                    html.Button(str(year), id=f'year-button-{year}', n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'}),
                dcc.Graph(id='bar-graph'),
            ], style={'width': '48%', 'padding': '0 1%'}),

            # Second graph
            html.Div([
                html.H3("Title 2"),
                html.Div([
                    html.Button(str(year), id=f'year-button-2-{year}', n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'}),
                dcc.Graph(id='scatter-graph')
                ], style={'width': '48%', 'padding': '0 1%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'}),

        # Add a break in the page for spacing
        html.Br(),

            # Third graph
            html.Div([
                html.H3("Title 3"),
                html.Div([
                    html.Button(str(year), id=f'year-button-3-{year}', n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'}),
                dcc.Graph(id='bar-graph-2')
            ], style={'width': '60%', 'margin': 'auto'}),
        ])
    
if __name__ == "__main__":
    run_app()