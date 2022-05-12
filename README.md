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
7.
