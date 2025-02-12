"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    archivo = "files/input/data.csv"
    diccionario = {}

    #LEE EL ARCHIVO
    with open(archivo, 'r') as file:
        for linea in file:
            #De cada fila crea una lista separa por '-', lo que da como resultado ['E\t1\t1999', '02', '28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2\n']. Y de ahí toma el primer elemento, osea el mes '02'
            mes = linea.split('-')[1]

            #Verifica si el mes existe como CLAVE en el diccionario, si es así le suma 1 al VALOR existente
            if mes in diccionario:
                diccionario[mes] += 1
            
            #Si el mes no existe como CLAVE en el diccionario, crea la CLAVE y un VALOR igual a 1 para dicha CLAVE
            else:
                diccionario[mes] = 1
    
    #Crea una lista ordenada que contiene tuplas como elementos
    respuesta = sorted(diccionario.items())
    return respuesta

impresion = pregunta_04()
print(impresion)
