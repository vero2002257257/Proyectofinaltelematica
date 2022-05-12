#Este código lo puedes utilizar si deseas
#1.Llamar las librerias
from dash import Dash, html, dcc  #LIBRERIA SERVIDOR
import pandas as pd

import plotly.graph_objs as go

#2.Base de datos
app = Dash(__name__)

def serve_layout():
  read = pd.read_excel('wikipagin.xlsx')

  return read.Div([html.H1(read['Titulo']),
               
                        html.Div(read['Tema']),
              
                        html.Div(read['Ayuda'])])


app.layout =serve_layout

if __name__ == '__main__':

  #Objeto a todas las interfaces de red en puerto 80
   app.run_server(host='0,0,0,0',port=80)
