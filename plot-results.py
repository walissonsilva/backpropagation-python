# encoding: utf-8

import plotly.plotly as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

def MSE_Nh():
    trace0 = go.Bar(
        x=['Nh = 2', 'Nh = 3', 'Nh = 4', 'Nh = 5', 'Nh = 6', 'Nh = 7', 'Nh = 8'],
        y=[0.00322535095676, 0.000758804236756, 0.000479361961268, 0.000342801720977, 0.000428509742598, 0.000616666676686, 0.00053375090329],
        marker=dict(
            color=['rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(12, 205, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)'],
            line=dict(
                width=1.5),
        ),
        opacity=0.5,
        width = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    )

    data = [trace0]
    layout = go.Layout(
        title='Mean Square Error (MSE)',
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='color-bar')

MSE_Nh()