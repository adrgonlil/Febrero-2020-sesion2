import csv
from collections import defaultdict, namedtuple
from datetime import datetime, date

Compra = namedtuple("Compra", "dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra")

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")

def lee_compras(fichero):
    res=[]
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            fecha_llegada=parsea_fecha(fecha_llegada)
            fecha_salida=parsea_fecha(fecha_salida)
            total_compra=float(total_compra)
            res.append(Compra(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra))
    return res

def compra_maxima_minima_provincia(compras, provincia=None):
    maximo=max(c.total_compra for c in compras if c.provincia==provincia or provincia is None)
    minimo=min(c.total_compra for c in compras if c.provincia==provincia or provincia is None)
    return(maximo, minimo)

def hora_menos_afluencia(compras):
    dicc=defaultdict(int)
    for c in compras:
        dicc[c.fecha_llegada.hour]+=1
    return min(dicc.items(), key=lambda x:x[1])

def supermercados_mas_facturacion(compras, n=3):
    dicc=dict()
    diccionario=defaultdict(float)
    for i in range(1,n+1):
        dicc[i]=0
    for c in compras:
        diccionario[c.supermercado]+=c.total_compra
    lista_ordenada=sorted(diccionario.items(), reverse=True, key=lambda x:x[1])
    for i in range(1,n+1):
        dicc[i]=lista_ordenada[i-1]
    return dicc.items()

def clientes_itinerantes(compras, n):
    dicc=defaultdict(set)
    diccionario=defaultdict(list)
    for c in compras:
        dicc[c.dni].add(c.provincia)
    for clave, conjunto in dicc.items():
        dicc[clave]=sorted(conjunto)
    for clave, lista in dicc.items():
        if len(lista)>n:
            diccionario[clave]=sorted(lista)
    return sorted(diccionario.items())

def dia_estrella(compras, super, provincia):
    

