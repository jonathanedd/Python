#Calcular el costo total de producción de un lote de pollos
#Incluyendo los costos de alimentación, alojamiento, y atención veterinaria

def lotePollos (chicken, food, hosting, vet):
    totalCost = chicken * (food + hosting + vet)
    print("El costo total de producción del lote de pollos teniend en cuenta alimentación, alojamiento y atención veterinaria es: ", totalCost)

chicken = int(input("Ingrese el numero de pollos: "))
food = int(input("Ingrese el total de alimentacipon: "))
hosting = int(input("Ingrese el total de alojamiento: "))
vet = int(input("Ingrese el costo total de la atención veterinaria: "))

lotePollos(chicken, food, hosting, vet)