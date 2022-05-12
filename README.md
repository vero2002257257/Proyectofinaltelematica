# Proyectofinaltelematica
Este es el proyecto final de telemática 

Pasos para realizarlo
1. clonar el repositorio con el siguiente comando y la URL especifica : git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
2. Iniciar el contenedor con este comando: sudo docker build -t proyectofinal:01 .
3. Ejecutar el servicio así: sudo docker run -it -p 80:80 proyectofinal:01 python3 app.py para hacerlo de forma interactiva
  sudo docker tun -d -p 80:80 proyectofinal:01 python3 app.py para que se corra por detrás 
4. Verificar que se creó de forma correcta: sudo docker ps 
5. Crear el archivo de tipo app.py para ejecutar los comandos necesarios : nano app.py
  Puede ser de este tipo 
from dash import Dash, html, dcc #Esta es la libreria para el servidor web del data science
import pandas as pd              #Esta libreria es para procesar los datos
import plotly.graph_objs as go

#Declarar objetos principales
app = Dash(__name__)


#Cargar la base de datos
def serve_layout():
  df = pd.read_excel('wikipagin.xlsx')
  return html.Div([html.H1(df['Titulo']),
                       html.Div(df['Tema']),
                       html.Div(df['Ayuda'])])
#funcion principal
app.layout = serve_layout

if __name__ == '__main__':
  #Cargar el objeto principal a todas las interfaces de red en el puerto 80
  app.run_server(host='0.0.0.0',port=80)
Este código lee un xlsx con 3 divisiones 
