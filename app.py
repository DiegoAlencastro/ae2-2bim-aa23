"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            # pass
            lineaDividida = row[0].split('|')
            numero =  lineaDividida[0]
            pagina = lineaDividida[1]
            print("Numero de pagina: %s  - URL: %s en archivo csv" % (numero, pagina ))
            lista.append((numero, pagina))
    # se retorna la lista con la información que se necesita
    time.sleep(2)
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # pass
    paginaRequest = requests.get(url)
    print("Url: %s - estado (200 ok): %s" % (url, paginaRequest.status_code ))
    archivo = open("salida/%s.txt" % numero,"w", encoding='utf-8')
    archivo.writelines(paginaRequest.text)
    archivo.close()
    print("Archivo creado de Url - %s" % (url))
    time.sleep(4)
    print("Finalizando %s numero: %s" % (threading.current_thread().getName(),numero))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='Navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()
