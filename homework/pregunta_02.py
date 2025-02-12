"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    archivo = "files/input/data.csv"
    diccionario = {}
     #LEE EL ARCHIVO
    with open(archivo, 'r') as file:
        for linea in file:
            #Por cada fila, toma la letra de la primera columna
            letra = linea.split('\t')[0]
            #La Letra es la clave del diccionario, si ya existe, le suma 1 al valor existente 'VALUES'
            if letra in diccionario:
                diccionario[letra] += 1
            #La Letra es la clave del diccionario, si no existe, le da el valor de 1 a 'VALUES'
            else:
                diccionario[letra] = 1
    #Crea una lista ordenada que contiene tuplas como elementos
    respuesta = sorted(diccionario.items())
    return respuesta

impr = pregunta_02()
print(impr)
