"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    archivo = "files/input/data.csv"
    diccionario = {}
 
    #LEE EL ARCHIVO

    with open(archivo, 'r') as file:
        for linea in file:
            fila = linea.split('\t')
            numeros = int(fila[1])
            letras = fila[3]
            letras = letras.split(',')
        
            for letra in letras:
                if letra in diccionario:
                    diccionario[letra] += numeros
                else:
                    diccionario[letra] = numeros

    return dict(sorted(diccionario.items()))

print(pregunta_11()) 

