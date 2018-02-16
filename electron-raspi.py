#!/usr/bin/python

# Internet of things - Alvaro Alvarez - Ed Krystosik
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11
# Lenguaje     : Python
# Dependencias : Libreria de Adafruit https://github.com/adafruit/Adafruit_Python_DHT


# Importa las librerias necesarias
import time
import datetime
import Adafruit_DHT

# folder to use
csv_path = "/var/log/iot/"

# Sensor Type AM2302
sensor = Adafruit_DHT.AM2302

# Configuracion del puerto GPIO al cual esta conectado (GPIO 4)
pin = 4

# Escribe un archivo CSV en csv_path con el nombre en el formato yyyy-mm-dd_dht.CSV
def write_csv(text):
    csv = open(csv_path + datetime.datetime.now().strftime("%Y-%m-%d") + "_dht.csv","a")
    line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + text + "\n"
    csv.write(line)
    csv.close()


# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:
    # Ciclo principal infinito
    #while True:
        # Obtiene la humedad y la temperatura desde el sensor
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

        # Si obtiene una lectura del sensor la registra en el archivo CSV
        if humedad is not None and temperatura is not None:
            ##write_csv( str(temperatura)+","+str(humedad))
            print '{0:0.1f}\n{1:0.1f}'.format(temperatura, humedad)
        else:
            print 'Error al obtener la lectura del sensor'

        # Wait  10 seconds before next capture (or 3600 to capture once an hour)
       # time.sleep(10)

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
    # Registra el error en el archivo csv y termina la ejecucion
    print str(e)
