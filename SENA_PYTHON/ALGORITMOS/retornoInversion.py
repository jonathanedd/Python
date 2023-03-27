#Ejercicio Calcular el ROI
# formula = "[(ingresos - inversion) / inversion ] x 100"

def investReturn(income, invest):
    netIncome = income - invest
    roi = (netIncome / invest) * 100
    print("La ganancia Neta de la inversión es: ", netIncome)
    print("y el porcentaje del retorno de la inversión es de", roi,"%" )

income=int(input("Cuanto es la ganancia neta: "))
invest=int(input("Cuanto fue la inversión: "))
investReturn(income, invest)