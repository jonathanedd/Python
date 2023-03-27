def investReturn(income, invest):
    # formula = "[(ingresos - inversion) / inversion ] x 100"
    netIncome = income - invest
    roi = (netIncome / invest) * 100
    print("La ganancia Neta de la inversión es: ", netIncome, "y el porcentaje del retorno de la inversión es de", roi,"%" )
    

income=int(input("Cuanto es la ganancia neta: "))
invest=int(input("Cuanto fue la inversión: "))
investReturn(income, invest)