"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    archivo = "files/input/data.csv"
    diccionario = {}
 
    #LEE EL ARCHIVO    
    #LOS COMENTARIOS LOS REALICÉ CON LA FILA 2 DEL DATA.CSV

    with open(archivo, 'r') as file:
        for linea in file:
            #Separa cada fila por '\t'(espacio) dando como resultado ['A', ... , 'ccc:2,ddd:0,aaa:3,hhh:9']
            fila = linea.strip().split('\t')
            #Toma cada clave ('A')
            clave = fila[0]
            #Hace una lista con los valores [2, 0, 3, 9]
            valores = fila[4]
            valores = [int(numeros.split(':')[1]) for numeros in valores.split(',')]

            #Toma elemento en la lista de VALORES
            for valor in valores:
                #Verifica si la Clave existe en el diccionario, si es así, solo suma la cantidad del valor
                if clave in diccionario:
                    diccionario[clave] += valor
                #Si no existe la Clave en el diccionario, añade el primer elemento de la lista valores a la correspondiente clave en el diccionario
                else:
                    diccionario[clave] = valores[0]
    
    return dict(sorted(diccionario.items()))

print(pregunta_12())


