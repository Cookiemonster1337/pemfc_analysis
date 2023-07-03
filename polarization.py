# PACKAGE IMPORT

from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px

# VARIABLE IMPORT
from overview import df_pol

#POLARIZATION-------------------------------------------------------------------------------------------

df_pol['current rounded'] = round(df_pol['current'], 1)

currents = df_pol['current rounded'].unique()

time = df_pol['Time Stamp']
voltage = df_pol['voltage']
current = df_pol['current']

temp_cell_an = df_pol['temp_anode_endplate']
temp_cell_cat = df_pol['temp_cathode_endplate']

# plot
fig = make_subplots(specs=[[{"secondary_y": True}]])
palette = px.colors.qualitative.Bold

traces_y1 = []
traces_y2 = []

# y-axis 1
traces_y1.append(go.Scatter(x=time, y=voltage, mode="lines", name='Cell Voltage', line=dict(color=palette[0])))

# y-axis 2
traces_y2.append(go.Scatter(x=time, y=current, mode="lines", name='Current Load', line=dict(color=palette[1])))
traces_y2.append(go.Scatter(x=time, y=temp_cell_cat, mode="lines", name='Cell Temperature',
                            line=dict(color=palette[2])))

for trace in traces_y1:
    fig.add_trace(trace, secondary_y=False)

for trace in traces_y2:
    fig.add_trace(trace, secondary_y=True)

plot(fig)