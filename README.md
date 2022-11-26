# SD_T3

## Servicio
Para poder levantar todos los servicios haremos uso del comando:
```sh
docker-compose up --build
```

## Hadoop
### MapReducer
#### Preparación de entorno
Para ejecutar el mapReducer hay que preparar el entorno, dando los permisos necesarios al usuario __hduser__ y creando la carpeta _"input"_ que almacena los archivos _.txt_ en los ficheros __Carpeta1__ y __Carpeta2__.
```sh
docker exec -it hadoop bash
cd examples
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input
hdfs dfs -put Wikipedia/Carpeta*/ input
sudo chown -R hduser .
```
Con los siguientes comandos se puede corroborar la preparación del _"input"_ y la asignación de permisos necesarios:
```sh
hdfs dfs -ls input
ls -la
```
#### Ejecución
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/Carpeta*/*.txt -output /user/hduser/output -mapper "python3.9 mapper.py" -reducer "python3.9 reducer.py"

hdfs dfs -cat /user/hduser/output/*
```
### Levantar API de archivos
```sh
python /home/hduser/examples/fileAPI.py 
```

## Video

<div style="text-align:left">
<a href="https://youtu.be/YKwF382gsJs">Link del Video</a>
</div>