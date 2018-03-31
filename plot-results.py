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
        title='Mean Square Error (MSE) x Nh',
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='color-bar')

def MSE_eta():
    trace0 = go.Bar(
        x=['0.005', '0.0075', '0.01', '0.0125', '0.01375', '0.014', '0.015', '0.01675', '0.0175'],
        y=[0.000651237838196, 0.000509132366308, 0.000342801720977, 0.000318285911086, 0.000285617184203, 0.000214122650244, 0.000226176626778, 0.000210204977508, 0.00291532537024],
        marker=dict(
            color=['rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(12, 205, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)', 'rgb(205, 12, 24)'],
            line=dict(
                width=1.5),
        ),
        opacity=0.5,
        #width = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    )

    data = [trace0]
    layout = go.Layout(
        title='Mean Square Error (MSE) x Taxa de Aprendizagem',
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='color-bar')

#MSE_Nh()
MSE_eta()