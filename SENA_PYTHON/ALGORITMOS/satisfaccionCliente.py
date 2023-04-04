#Escribe una función que calcule el índice de satisfacción del cliente basado en las calificaciones recibidas. 5Pts
#FORMULA : Suma de las puntualiones / total de valoraciones = indice de satisfaccion del cliente

def csat (rates):
    if rates >= 4 and rates <= 5:
        print("Your CSAT is Satisfied!")
    elif rates == 3:
        print("Your CSAT is Normal!")
    else: 
        print("Your CSAT is Bad!")

rates = int(input("From 1 to 5 how satisfied are you wth the service ? : "))
csat(rates)