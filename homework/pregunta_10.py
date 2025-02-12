"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    archivo = "files/input/data.csv"
    lista = []
 
    #LEE EL ARCHIVO

    with open(archivo, 'r') as file:
        for linea in file:
            #SEPARA CADA FILA COMO UNA COLUMNA ('E' , .... , 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2')
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            columna4 = columnas[3]
            columna5 = columnas[4]
        
            #CUENTA CUANTOS ELEMENTOS HAY EN LA COLUMNA 4 Y COLUMNA 5
            cantidad_columna4 = len(columna4.split(','))
            cantidad_columna5 = len(columna5.split(','))

            #AÑADE LAS VARIABLES A UNA LISTA
            lista.append((letra,cantidad_columna4,cantidad_columna5))
    
    return lista

print(pregunta_10())
        
