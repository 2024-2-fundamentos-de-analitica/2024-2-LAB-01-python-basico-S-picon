"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    archivo = "files/input/data.csv"
    diccionario = {}

    #LEE EL ARCHIVO
    with open(archivo, 'r') as file:
        for linea in file:
            #De cada fila toma la letra en la columna 0 (o 1 depende como usted inicie el conteo)
            letra = linea.split('\t')[0]
            #De cada fila toma el numero<<como string>> en la columna 1 (o 2 depende como usted inicie el conteo)
            numero = linea.split('\t')[1]

            #Verifica si la letra está como CLAVE en el diccionario, si es así, añade al VALOR que es una lista de numeros ese nuevo numero
            if letra in diccionario:
                diccionario[letra].append(int(numero))

            #Si la letra NO está como CLAVE en el diccionario, crea un VALOR que es una lista de numeros
            else:
                diccionario[letra] = [int(numero)]
    
    #Va a tomar el diccionaro CLAVE<<letra>>,VALOR<<lista de numeros>> y lo va a convetir en una LISTA de Tuplas ordenadas, y de ahí va a tomar el maximo y el minimo
    respuesta = [(letra, max(numero), min(numero))
                 for letra,numero in sorted(diccionario.items())]
    return respuesta

impresion = pregunta_05()
print(impresion)
