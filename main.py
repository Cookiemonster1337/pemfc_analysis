# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:36:18 2023

@author: j.kapp
"""

from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import os

path = r'C:\Users\j.kapp\Desktop\gts_data'

csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]

dfs = {}

for file in csv_files:
    df_file = pd.read_csv(os.path.join(path, file), encoding='cp1252', skiprows=17)
    dfs[file] = df_file

df = pd.concat(dfs.values(), ignore_index=True)

pol_marker = df[df['File Mark'] == 'polcurve_1'].index.tolist()
eis_marker = df[df['File Mark'] == 'eis_low'].index.tolist()
poldata = df[pol_marker[0]:eis_marker[0]]
nom_marker = poldata[poldata['File Mark'] == 'nom_op'].index.tolist()
poldata = df[pol_marker[0]:nom_marker[0]]
poldata['current rounded'] = round(poldata['current'], 1)
jmax = round(poldata['current'], 2).max()
jmax_marker = poldata[round(poldata['current'], 2) == jmax].index.tolist()

poldata_inc = poldata[:jmax_marker[-1]]
poldata_dec = poldata[jmax_marker[0]:]

print(poldata_inc[poldata_inc['current rounded'] == 20]['voltage'])
currents = [0, 0.5, 1, 1.5, 2, 2.5, 5, 7.5, 10, 12.5, 15, 20, 25, 30, 35, 40, 45, jmax]

voltages = []

for j in currents:
    voltage = poldata_inc[poldata_inc['current rounded'] == j]['voltage']

    voltages.append(voltage[-100:0].mean())

fig = make_subplots(specs=[[{"secondary_y": True}]])

traces = []
palette = px.colors.qualitative.Bold

traces.append(go.Scatter(x=currents, y=voltages, mode="lines",
                         # name=sample,
                         # visible=False,
                         line=dict(color=palette[0])))

for trace in traces:
    fig.add_trace(trace)

# i = 0
# pol_voltage = poldata['voltage']
# pol_time = poldata['Time Stamp']
# pol_current= poldata['current']

# traces.append(go.Scatter(x=pol_time, y=pol_voltage, mode="lines",
#                           # name=sample,
#                           # visible=False,
#                           line=dict(color=palette[0])))
# traces.append(go.Scatter(x=pol_time, y=pol_current, mode="lines",
#                           # name=sample,
#                           # visible=False,
#                           line=dict(color=palette[1])))

# i = 1
# for trace in traces:
#     if i%2 == 0:
#         fig.add_trace(trace, secondary_y=True)
#     else:
#         fig.add_trace(trace, secondary_y=False)
#     i += 1

plot(fig)
