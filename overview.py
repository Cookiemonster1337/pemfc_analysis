# PACKAGE IMPORT

from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import os


# CREATE DATAFRAME FROM CSV-FILES
path = 'gts_data'
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
dfs = {}
for file in csv_files:
    df_file = pd.read_csv(os.path.join(path, file), encoding='cp1252', skiprows=17, low_memory=False)
    dfs[file] = df_file
df = pd.concat(dfs.values(), ignore_index=True)

# GET SETMARKER
setmarker = df[df['File Mark'].notnull()]['File Mark']

# data
cond_marker = df[df['File Mark'] == 'Conditioning']['Time Stamp'].tolist()
char_marker = df[df['File Mark'] == 'Characterization']['Time Stamp'].tolist()
pol_marker = df[df['File Mark'] == 'polcurve_1']['Time Stamp'].tolist()
eis_low_marker = df[df['File Mark'] == 'eis_low']['Time Stamp'].tolist()
eis_med_marker = df[df['File Mark'] == 'eis_med']['Time Stamp'].tolist()
# eis_high_marker = df[df['File Mark'] == 'eis_high']['Time Stamp'].tolist()


df_cond = df[(df['Time Stamp'] >= cond_marker[0]) & (df['Time Stamp'] < char_marker[0])]
df_pol = df[(df['Time Stamp'] >= pol_marker[0]) & (df['Time Stamp'] < eis_low_marker[0])]
df_eis = df[(df['Time Stamp'] >= eis_low_marker[0]) & (df['Time Stamp'] < eis_med_marker[0])]
# df_pol = df[(df['Time Stamp'] >= pol_marker[0]) & (df['Time Stamp'] < eis_low_marker[0])]
# df_pol = df[(df['Time Stamp'] >= pol_marker[0]) & (df['Time Stamp'] < eis_low_marker[0])]

#COMPLETE EXP DATA-------------------------------------------------------------------------------------------

time = df['Time Stamp']
voltage = df['voltage']
current = df['current']

temp_cell_an = df['temp_anode_endplate']
temp_cell_cat = df['temp_cathode_endplate']

pressure_an = df['pressure_anode_inlet']
pressure_cat = df['pressure_cathode_inlet']

flow_an = df['total_anode_stack_flow']
flow_cat = df['total_cathode_stack_flow']

# plot
fig_overview = make_subplots(specs=[[{"secondary_y": True}]])
palette = px.colors.qualitative.Bold

traces_y1 = []
traces_y2 = []

# y-axis 1
traces_y1.append(go.Scatter(x=time, y=voltage, mode="lines", name='Cell Voltage', line=dict(color=palette[0]), yaxis='y1'))
traces_y1.append(go.Scatter(x=time, y=flow_an, mode="lines", name='Flowrate Anode', line=dict(color=palette[5]), yaxis='y1'))
traces_y1.append(go.Scatter(x=time, y=flow_cat, mode="lines", name='Flowrate Cathode', line=dict(color=palette[6]), yaxis='y1'))

# y-axis 2
traces_y2.append(go.Scatter(x=time, y=current, mode="lines", name='Current Load', line=dict(color=palette[1]), yaxis='y2'))
traces_y2.append(go.Scatter(x=time, y=temp_cell_cat, mode="lines", name='Cell Temperature',
                            line=dict(color=palette[2]), yaxis='y2'))
traces_y2.append(go.Scatter(x=time, y=pressure_an, mode="lines", name='Pressure Anode', line=dict(color=palette[3]), yaxis='y2'))
traces_y2.append(go.Scatter(x=time, y=pressure_cat, mode="lines", name='Pressure Cathode', line=dict(color=palette[4]), yaxis='y2'))

# for trace in traces_y1:
#     fig_overview.add_trace(trace, secondary_y=False)
#
# for trace in traces_y2:
#     fig_overview.add_trace(trace, secondary_y=True)

overview_data = traces_y1 + traces_y2
# pol_marker = df[df['File Mark'] == 'polcurve_1'].index.tolist()
# eis_marker = df[df['File Mark'] == 'eis_low'].index.tolist()
# poldata = df[pol_marker[0]:eis_marker[0]]
# nom_marker = poldata[poldata['File Mark'] == 'nom_op'].index.tolist()
# poldata = df[pol_marker[0]:nom_marker[0]]
# poldata['current rounded'] = round(poldata['current'], 1)
# jmax = round(poldata['current'], 2).max()
# jmax_marker = poldata[round(poldata['current'], 2) == jmax].index.tolist()
#
# poldata_inc = poldata[:jmax_marker[-1]]
# poldata_dec = poldata[jmax_marker[0]:]
#
# print(poldata_inc[poldata_inc['current rounded'] == 20]['voltage'])
# currents = [0, 0.5, 1, 1.5, 2, 2.5, 5, 7.5, 10, 12.5, 15, 20, 25, 30, 35, 40, 45, jmax]
#
# voltages = []
#
# for j in currents:
#     voltage = poldata_inc[poldata_inc['current rounded'] == j]['voltage']
#
#     voltages.append(voltage[-100:0].mean())
#
# fig = make_subplots(specs=[[{"secondary_y": True}]])
#
# traces = []
# palette = px.colors.qualitative.Bold
#
# traces.append(go.Scatter(x=currents, y=voltages, mode="lines",
#                          # name=sample,
#                          # visible=False,
#                          line=dict(color=palette[0])))
#
# for trace in traces:
#     fig.add_trace(trace)
#
# # i = 0
# # pol_voltage = poldata['voltage']
# # pol_time = poldata['Time Stamp']
# # pol_current= poldata['current']
#
# # traces.append(go.Scatter(x=pol_time, y=pol_voltage, mode="lines",
# #                           # name=sample,
# #                           # visible=False,
# #                           line=dict(color=palette[0])))
# # traces.append(go.Scatter(x=pol_time, y=pol_current, mode="lines",
# #                           # name=sample,
# #                           # visible=False,
# #                           line=dict(color=palette[1])))
#
# # i = 1
# # for trace in traces:
# #     if i%2 == 0:
# #         fig.add_trace(trace, secondary_y=True)
# #     else:
# #         fig.add_trace(trace, secondary_y=False)
# #     i += 1
#
# plot(fig)
