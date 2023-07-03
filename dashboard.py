import dash

from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# DATA IMPORT
from data_aquisition import data_overview, data_pol, data_eis
from dash_functions import drawIcon, drawTextTitle, drawFigureTestrig, drawPlaceholder, drawDropDown, drawRadioItems


data_select = ''
# INIT DASH
app = dash.Dash(__name__)

# DASH LAYOUT

#ZBT color scheme
colors = {'zbt':'#005EB8'}

#External Color Scheme
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

#Page Layout
app.layout = dbc.Container([
    dbc.Card(
        dbc.CardBody([
#ROW 1 ---------------------------------------------------------------------------------------------------------------
            dbc.Row([
#ROW 1 / COL1  -----------------------------------------------------------------------------------------
                dbc.Col([
                    drawIcon()
                ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                ),
#ROW 1 / COL2  -----------------------------------------------------------------------------------------
                dbc.Col([
                    drawTextTitle()
                ], width=10, style={'background':  colors['zbt'], 'padding': '2px'}
                ),
            ], align='center',
            ),
#ROW 2 ---------------------------------------------------------------------------------------------------------------
            dbc.Row([
#ROW 2 / COL1  -----------------------------------------------------------------------------------------
                dbc.Col([

                    drawDropDown()
                ], width=4, style={'background': colors['zbt'], 'padding': '2px'}
                ),
#ROW 2 / COL2  -----------------------------------------------------------------------------------------
                dbc.Col([
                    drawRadioItems()
                ], width=8, style={'background':  colors['zbt'], 'padding': '2px'}
                ),
            ], align='center'
            ),
#ROW 3 ---------------------------------------------------------------------------------------------------------------
            dbc.Row([
#ROW 3 / COL1  -----------------------------------------------------------------------------------------
                dbc.Col([
                    dbc.Row([
                        drawFigureTestrig()
                    ], style={'background': colors['zbt'], 'padding': '2px'}
                    ),
                    # dbc.Row([
                    #     # drawTableParameterPOL()
                    # ], style={'background': colors['zbt'], 'padding': '2px'}
                    # )
                ], width=12, style={}
                ),
# #ROW 3 / COL2  -----------------------------------------------------------------------------------------
#                 dbc.Col([
#                     drawFigureTestrig()
#                 ], width=9, style={'background':  colors['zbt'],  'padding': '2px'}
#                 ),
#ROW 3 / COL3  -----------------------------------------------------------------------------------------
                # dbc.Col([
                #     # drawTestrigSummary()
                # ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                # ),
            ], align='center',
            ),
        ], style={'background': colors['zbt'], 'padding': '0px'
                  }),
    )
], fluid=True
)

# APP CALLBACKS -------------------------------------------------------------------------------------------------------
@app.callback(
    dash.dependencies.Output('graph_1', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('radio', 'value')
    ]
)

def updateFigure(dropdown_value, radio_value):
    print(dropdown_value, radio_value)
    if radio_value=='total':
        fig_data = data_overview(dropdown_value)
    if radio_value=='pol':
        fig_data = data_pol(dropdown_value)
    if radio_value == 'eis':
        fig_data = data_eis(dropdown_value)

    figure = go.Figure(fig_data).update_layout(
                            template='plotly_dark',
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                            title='Testbench-Parameter Monitoring',
                            xaxis=dict(title='duration [h]'),
                            yaxis=dict(title='current density [A/cm2]'),
                            yaxis2=dict(title='parameter selection', overlaying='y', side='right'),
                            legend={"x": 1.1, 'y': 1.4}
    )
    return figure


# def update_graph(selected_value):
#     file = selected_value
#
#     # figure = go.Figure(data=overview_data).update_layout(
#     #     template='plotly_dark',
#     #     plot_bgcolor='rgba(0, 0, 0, 0)',
#     #     paper_bgcolor='rgba(0, 0, 0, 0)',
#     #     title='Testbench-Parameter Monitoring',
#     #     xaxis=dict(title='duration [h]'),
#     #     yaxis=dict(title='current density [A/cm2]'),
#     #     yaxis2=dict(title='parameter selection', overlaying='y', side='right'),
#     #     legend={"x": 1.1, 'y': 1.4}
#
#     return drawFigureTestrig(file)
# def update_output(value):
#     data_select = value
#     # return data_select






# # DEFINE CALLBACKS (INTERACTIVITY)
# @app.callback(
#     Output('example-graph', 'figure'),
#     [Input('input-id', 'value')]  # Add input components as needed
# )
# def update_graph(input_value):
#     # Perform necessary calculations or data manipulations
#     # Update the figure object and return it
#     return {
#         'data': [
#             {'x': [1, 2, 3], 'y': [input_value, 2 * input_value, 3 * input_value], 'type': 'bar', 'name': 'Data'}
#         ],
#         'layout': {
#             'title': 'Updated Graph'
#         }
#     }

# RUN DASH
app.run_server(debug=True, port=8000)