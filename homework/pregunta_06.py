"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    archivo = "files/input/data.csv"
    diccionario = {}

    with open(archivo, 'r') as file:
        for linea in file:
            cadena = linea.split('\t')[4].strip()
            numeros = cadena.split(',')
            
            for num in numeros:
                clave, valor = num.split(':')
                valor = int(valor)

                if clave in diccionario:
                    diccionario[clave].append(valor)
                else:
                    diccionario[clave] = [valor]
    
    respuesta = [(clave, min(diccionario[clave]), max(diccionario[clave]))
                 for clave in sorted(diccionario.keys())]
    return respuesta

impresion = pregunta_06()
print(impresion)
