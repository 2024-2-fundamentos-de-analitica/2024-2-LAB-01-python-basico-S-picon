"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

archivo = "files/input/data.csv"

def pregunta_01():

    contador = 0
     #LEE EL ARCHIVO
    with open(archivo, 'r') as file:
        for linea in file:
            #Hace una lista de cada fila donde los elementos son las columnas
            linea = linea.split('\t')
            #Suma la columna 2 de cada fila
            contador += int(linea[1])
    
    return contador

respuesta = pregunta_01()
print(respuesta)

"""
Retorne la suma de la segunda columna.

Rta/
214

"""
    
