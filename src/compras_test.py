from compras import *

def muestra_iterable(iterable):
    for elem in iterable:
        print(elem)

def test_lee_compras(datos):
    print("Hay", len(datos), "datos")
    print("Estos son los dos primeros datos:")
    muestra_iterable(datos[:2])
    print("Estos son los dos ultimos datos:")
    muestra_iterable(datos[-2:])


def test_compra_maxima_minima_provincia(datos):
    print("Importe máximo para la provincia de huelva:", compra_maxima_minima_provincia(datos,"Huelva")[0],\
        "importe mínimo:", compra_maxima_minima_provincia(datos, "Huelva")[1])





if __name__ == "__main__":
    compras=lee_compras("data/compras.csv")
    test_lee_compras(compras)
    test_compra_maxima_minima_provincia(compras)
    print(hora_menos_afluencia(compras))
    print(supermercados_mas_facturacion(compras,2))
    print(clientes_itinerantes(compras,7))