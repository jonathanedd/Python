#Crea una función que calcule el beneficio neto de una empresa en función de sus ingresos y gastos.  5Pts
def benefit(total, cost):
    benefit = cost - total
    print("El beneficio total de las ventas es de: ", benefit)


cost = int(input("Ingrese el Costo del producto:"))
total = int(input("Ingrese el monto de venta por producto:"))
benefit(cost, total)
