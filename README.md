Pequeña pratica de docker

se creo una pequeña aplicacion rest en flask, para despues crear un contenedor docker.

*Nota: para levantar el entorno virtual de python en windows, se ejecuta el comando:  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

comandos de docker:

docker build -t flaskapp .
docker run -it flaskapp /bin/sh
docker run -it --publish 7000:4000 flaskapp
