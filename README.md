# RaspberryPi-AM2302 Sensor
Programas ejemplo de como conectar el sensor de temperatura y humedad AM2302 a una Raspberry Pi 3.

## Software Necesario
- Librerias de desarrollo Python y cliente MySQL

  sudo apt-get install python-pip python-dev libmysqlclient-dev

- Libreria Python MySQLdb

  sudo pip install MySQL-python

- Libreria de Adafruit Python DHT, disponible en https://github.com/adafruit/Adafruit_Python_DHT



## Base de datos
El programa dht_mysql.py escribe los registros en una base de datos MySQL, para crear la tabla datos se debe usar el script SQL ubicado en la carpeta sql


## Basado en: http://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-AM2302/


