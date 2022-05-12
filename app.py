#Este código lo puedes utilizar si deseas
#1.Llamar las librerias
from dash import Dash, html, dcc
import plotly.graph objs as go
import pandas as pd

app = Dash(_name_)

def serve_layout():
read = pd.read_excel('wikipagin.xlsx')

return read.Div([html.H1(read['Titulo']),
               
html.Div(read['Tema']),

html.Div(read['Info']),
              
html.Div(read['Ayuda'])])])


app.layout =serve_layout

if_name== 'main_':

app.run_server(host='0,0,0,0',port=80)
