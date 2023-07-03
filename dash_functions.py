from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from main import test_dirs
from data_aquisition import data_overview


# function - ZBT Icon
def drawIcon():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.Img(src='assets/ZBT_Logo_RGB_B_S_cropped.png',
                             style={'height': '45px', 'width': 'auto', 'max-width': '100%'}
                    )
                ],
                )
            ], style={'textAlign': 'center', 'height': '80px'}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

# function - Textbox
def drawTextTitle():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("PEMFC operando analysis"),
                ], style={'textAlign': 'center', 'color': 'white'}
                )
            ], style={'height': '80px'}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )



# FUNCTION - DRAW PLACEHOLDER

def drawPlaceholder(text=''):
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H6(text)
                ], style={
                    'textAlign': 'center', 'color': 'white'
                }
                )
            ], style={
            }
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# FUNCTION - draw DropDown-Menu for selection of test-files to plot
def drawDropDown():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dbc.Label('Select Test:', style={'margin-bottom': '10px'}),
                dcc.Dropdown(id='dropdown',
                    options=[
                        {'label': str(entry).split('\\')[-1], 'value': str(entry)} for entry in test_dirs
                    ],
                    value=test_dirs[0]  # set the initial value
                ),
                # html.Div(id='output')  # a placeholder to display the selected value
            ],
            style={'height': '100px'}
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# FUNCTION - draw RadioItems for selection of data to plot
def drawRadioItems():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dbc.Label('Select Plot:', style={'margin-bottom': '10px'}),
                dcc.RadioItems(id='radio',
                    options=[
                        {'label': 'Total Data', 'value': 'total'},
                        {'label': 'POL', 'value': 'pol'},
                        {'label': 'EIS', 'value': 'eis'},
                        {'label': 'CV', 'value': 'cv'},
                        {'label': 'DEG', 'value': 'deg'},
                    ],
                    value='total',
                    inputStyle={'margin-left': '50px', 'margin-right': '10px'}
                ),
                # html.Div(id='output2')  # a placeholder to display the selected value
            ],
            style={'height':'100px'}
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# function - Overview Figure
def drawFigureTestrig():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(id='graph_1'
                    )
            ], style={
                'height': '450px'
            }
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )