# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:50:00 2023

@author: j.kapp
"""

from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
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

# file = '0 - 230627 101655 - part_1.csv'

# df = pd.read_csv(os.path.join(path, file), encoding='cp1252', skiprows=17)



fig = make_subplots(specs=[[{"secondary_y": True}]])

traces = []
palette = px.colors.qualitative.Bold
i = 0

voltage = df['voltage']
elapsed = df['Elapsed Time']
time = df['Time Stamp']

traces.append(go.Scatter(x=time, y=voltage, mode="lines",
                         # name=sample,
                         # visible=False,
                         line=dict(color=palette[i])))
# traces.append(go.Scatter(x=x_pores, y=y2_volume, mode="lines",
#                          legendgroup=sample,
#                          name=sample + ' dV/dlog',
#                          # visible=False,
#                          line=dict(color=palette[i], dash='dash')))


for trace in traces:
    fig.add_trace(trace, secondary_y=False)


plot(fig)