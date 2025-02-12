"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    archivo = "files/input/data.csv"
    diccionario = {}

    with open(archivo, 'r') as file:
        for linea in file:
            cadena = linea.split('\t')[4].strip()
            numeros = cadena.split(',')
            
            for num in numeros:
                clave, valor = num.split(':')
                valor = 1

                if clave in diccionario:
                    diccionario[clave].append(valor+1)
                else:
                    diccionario[clave] = [valor]
    
    respuesta = {(clave, len(diccionario[clave]))
                 for clave in sorted(diccionario.keys())}
    return dict(sorted(respuesta))

impresion = pregunta_09()
print(impresion)
