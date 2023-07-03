import os
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# FUNCTION - aquire data based on test-selection (complete dataset)
def get_data(select_dir=None):
    if select_dir == None:
        test_data_df = []
    else:
        # read csv-files of selected data-folder and create one contigous dataframe
        csv_files = [f for f in os.listdir(select_dir)]
        test_data_dfs = {}
        for file in csv_files:
            df_file = pd.read_csv(os.path.join(select_dir, file), encoding='cp1252', skiprows=17, low_memory=False)
            test_data_dfs[file] = df_file
        test_data_df = pd.concat(test_data_dfs.values(), ignore_index=True)
    return test_data_df

def get_traces(test_data_df=None):
    # read in values of interest for plotting from dataframe
    time = test_data_df['Time Stamp']
    voltage = test_data_df['voltage']
    current = test_data_df['current']

    temp_cell_an = test_data_df['temp_anode_endplate']
    temp_cell_cat = test_data_df['temp_cathode_endplate']

    pressure_an = test_data_df['pressure_anode_inlet']
    pressure_cat = test_data_df['pressure_cathode_inlet']

    flow_an = test_data_df['total_anode_stack_flow']
    flow_cat = test_data_df['total_cathode_stack_flow']

    # create traces from values for plot
    fig_overview = make_subplots(specs=[[{"secondary_y": True}]])
    palette = px.colors.qualitative.Bold

    traces_y1 = []
    traces_y2 = []

    # y-axis 1
    traces_y1.append(
        go.Scatter(x=time, y=voltage, mode="lines", name='Cell Voltage', line=dict(color=palette[0]), yaxis='y1'))
    traces_y1.append(
        go.Scatter(x=time, y=flow_an, mode="lines", name='Flowrate Anode', line=dict(color=palette[5]), yaxis='y1'))
    traces_y1.append(
        go.Scatter(x=time, y=flow_cat, mode="lines", name='Flowrate Cathode', line=dict(color=palette[6]),
                   yaxis='y1'))

    # y-axis 2
    traces_y2.append(
        go.Scatter(x=time, y=current, mode="lines", name='Current Load', line=dict(color=palette[1]), yaxis='y2'))
    traces_y2.append(go.Scatter(x=time, y=temp_cell_cat, mode="lines", name='Cell Temperature',
                                line=dict(color=palette[2]), yaxis='y2'))
    traces_y2.append(
        go.Scatter(x=time, y=pressure_an, mode="lines", name='Pressure Anode', line=dict(color=palette[3]),
                   yaxis='y2'))
    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat, mode="lines", name='Pressure Cathode', line=dict(color=palette[4]),
                   yaxis='y2'))

    # gather traces in a list which is given to dash-layout-function (drawTestFigureRig)
    traces = traces_y1 + traces_y2

    return traces


# FUNCTION --> DATA for MAIN PLOT in DASHBOARD -------------------------------------------------------------------------

def data_overview(select_dir):
    test_data_df = get_data(select_dir)
    overview_data = get_traces(test_data_df)
    return overview_data


# FUNCTION --> DATA for POL in DASHBOARD -------------------------------------------------------------------------------

def data_pol(select_dir):

    # get test data of csv-files as dataframe via corresponding function
    test_data_df = get_data(select_dir)

    # get beginning and end of polarization procedure in test-dataframe
    pol_marker = test_data_df[test_data_df['File Mark'] == 'polcurve_1']['Time Stamp'].tolist()
    eis_low_marker = test_data_df[test_data_df['File Mark'] == 'eis_low']['Time Stamp'].tolist()

    pol_data_df = test_data_df[(test_data_df['Time Stamp'] >= pol_marker[0]) &
                          (test_data_df['Time Stamp'] < eis_low_marker[0])]

    pol_data = get_traces(pol_data_df)

    return pol_data


# FUNCTION --> DATA for POL in DASHBOARD -------------------------------------------------------------------------------

def data_eis(select_dir):

    # get test data of csv-files as dataframe via corresponding function
    test_data_df = get_data(select_dir)

    # get beginning and end of polarization procedure in test-dataframe and extract relevant data-snippet
    eis_low_marker = test_data_df[test_data_df['File Mark'] == 'eis_low']['Time Stamp'].tolist()
    eis_med_marker = test_data_df[test_data_df['File Mark'] == 'eis_med']['Time Stamp'].tolist()


    eis_data_df = test_data_df[(test_data_df['Time Stamp'] >= eis_low_marker[0]) &
                          (test_data_df['Time Stamp'] < eis_med_marker[0])]

    eis_data = get_traces(eis_data_df)
    pd.set_option('display.max_columns', None)
    print(eis_data_df.head)
    return eis_data





