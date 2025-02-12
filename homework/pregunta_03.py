"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    archivo = "files/input/data.csv"
    diccionario = {}
    #LEE EL ARCHIVO
    with open(archivo, 'r') as file:
        for linea in file:
            #Por cada fila, toma la letra de la columna 0 (o 1, depende como usted inicie la cuenta)
            letra = linea.split('\t')[0]
            #Por cada fila, toma el numero de la columna 1 (o 2, depende como usted inicie la cuenta)
            numero = linea.split('\t')[1]
            
            #Verifica si la letra existe en el diccionario como una clave, si es así, le suma el valor de la variable NUMERO al numero ya existente
            if letra in diccionario:
                diccionario[letra] += int(numero)
                
            #Si no existe letra como una clave en el diccionario, le asigna el valor de numero a dicha clave (Ejemplo iteración 1: como 'E' no existe como CLAVE en el dict, asigna el valor de '1', teniedo la CLAVE, VALOR en el dict de 'E':1)
            else:
                diccionario[letra] = int(numero)
    
    #Crea una lista ordenada que contiene tuplas como elementos
    respuesta = sorted(diccionario.items())
    return respuesta

impresion = pregunta_03()
print(impresion)