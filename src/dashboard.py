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
    "Chicago Bears": "#002244",
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
    "Washington Commanders": "#420D09",
    "Washington Football Team": "#420D09",
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
                       'fontSize': '60px',
                       'margin': '20px 0'
                       }),

        html.Label("Select Side of the Ball (Offense/Defense):"),
        dcc.Dropdown(
            id='side-dropdown',
            options=[
                {'label': 'Offense', 
                 'value': 'Offense'},
                {'label': 'Defense', 
                 'value': 'Defense'}
            ],
            value='Offense',
            clearable=False,
            style={'width': '150px', 
                   'padding': '0 10px'
                   }
            ),
        
        # Add a break in the page for spacing
        html.Br(),

        # Set up the layout for the graphs
        html.Div([
            # First graph layout
            html.Div([
                html.H3("Points Overview"),
                html.Div([
                    html.Button(str(year), 
                                id=f'year-button-{year}', 
                                n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'
                          }),
                dcc.Graph(id='bar-graph'),
            ], style={'width': '48%', 
                      'padding': '0 1%'}),

            # Second graph layout
            html.Div([
                html.H3("Team Performance"),
                html.Div([
                    html.Button(str(year), 
                                id=f'year-button-2-{year}', 
                                n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'
                          }),
                dcc.Graph(id='scatter-plot')
                ], style={'width': '48%', 
                          'padding': '0 1%'})
        ], style={'display': 'flex', 
                  'justify-content': 'space-between'}),

        # Add a break in the page for spacing
        html.Br(),

            # Third graph layout
            html.Div([
                html.H3("Title 3"),
                html.Div([
                    html.Button(str(year), 
                                id=f'year-button-3-{year}', 
                                n_clicks=0)
                    for year in all_years
                ], style={'display': 'flex', 
                          'justifyContent': 'center',
                          'flexWrap': 'wrap',
                          'gap': '10px',
                          'margin': 'auto'
                          }),
                dcc.Graph(id='bar-graph-2')
            ], style={'width': '60%', 
                      'margin': 'auto'}),

        html.Div([
            html.P("This dashboard is created using Dash and Plotly. "
                "Created by Tommy Burkett, 2025", 
                style={'textAlign': 'center', 
                       'fontSize': '15px', 
                       'margin': '20px 0'}),
            
            # Source text with links
            html.P("Source: NFL Data from 2020-2024 ",
                style={'textAlign': 'center', 
                       'fontSize': '15px', 
                       'margin': '20px 0'}),
            
            html.P([
                html.A("Pro Football Reference", 
                       href="https://www.pro-football-reference.com/", 
                       target="_blank"),
                " & ",
                html.A("NFL.com", 
                       href="https://www.nfl.com/stats/", 
                       target="_blank")
            ], style={'textAlign': 'center', 
                      'fontSize': '15px', 
                      'margin': '20px 0'})
        ], style={'textAlign': 'center', 
                  'fontSize': '15px', 
                  'color': '#555'})
    ])
    
# Callbacks
@callback(
    Output('bar-graph', 'figure'),
    Input('side-dropdown', 'value'),
    [Input(f'year-button-{year}', 'n_clicks') for year in all_years]
)
def update_bar(side: str,
               *n_clicks: int
              ) -> go.Figure:
    
    # Get the year from the button that was clicked
    if not any(n_clicks):
        selected_year = all_years[-1]
    else:
        max_clicks = np.argmax(n_clicks)
        selected_year = all_years[max_clicks]
    # Filter dataframe based on selected year and side
    df_filtered = df[(df['Year'] == selected_year) & (df['Side'] == side)]

    # Differentiate between offense and defense
    if side == 'Offense':
        x = 'Team'
        y = 'Points For'
        title = f'Offensive Points Scored by Team ({selected_year})'
    else:
        x = 'Team'
        y = 'Points Allowed'
        title = f'Defensive Points Allowed by Team ({selected_year})'

    # Create the bar plot
    fig = px.bar(df_filtered,
                 x=x, 
                 y=y, 
                 color='Team',
                 color_discrete_map=team_colors,
                 title=title
                 )
    
    # Update the layout
    fig.update_layout(xaxis_title=x,
                      yaxis_title=y,
                      legend_title='Team',
                      title_x=0.5,
                      title_y=0.95,
                      xaxis_tickangle=-90,
                      showlegend=False,
                      height=500
                     )
    
    return fig


# Callbacks
@callback(
    Output('scatter-plot', 'figure'),
    Input('side-dropdown', 'value'),
    [Input(f'year-button-2-{year}', 'n_clicks') for year in all_years]
)
def update_scatter(side: str,
                   *n_clicks: int
                  ) -> go.Figure:
    
    # Get the year from the button that was clicked
    if not any(n_clicks):
        selected_year = all_years[-1]
    else:
        max_clicks = np.argmax(n_clicks)
        selected_year = all_years[max_clicks]
    # Filter dataframe based on selected year and side
    df_filtered = df[(df['Year'] == selected_year) & (df['Side'] == side)]

    # Differentiate between offense and defense
    if side == 'Offense':
        x = 'Passing Yards'
        y = 'Rushing Yards'
        title = f'Offensive Passing Yards vs Rushing Yards ({selected_year})'
    else:
        x = 'Total Yards'
        y = 'Points Allowed'
        title = f'Defensive Total Yards vs Points Allowed ({selected_year})'

    # Create the scatter plot
    fig = px.scatter(df_filtered,
                     x=x,
                     y=y,
                     color='Team',
                     hover_name='Team',
                     color_discrete_map=team_colors,
                     title=title
                    )
    
    # Update the layout
    fig.update_layout(xaxis_title=x,
                      yaxis_title=y,
                      legend_title='Team',
                      title_x=0.5,
                      title_y=0.95,
                      showlegend=False,
                      height=500
                     )
    
    return fig

if __name__ == "__main__":
    run_app()