#Calcular el costo de una obra de construccion
#fórmula: COSTOS DIRECTOS + COSTOS INDIRECTOS = COSTO TOTAL
def costo_obra (direct, indirect):
    total = direct + indirect
    print("Total costo de la Obra: ", total)

#Se le pide al usuario que ingrese de los costos directos e indirectos, se calculan con una suma
print("COSTOS DIRECTOS")
direct = int(input("Total mano de Obra: " )) + int(input("Total Materiales: ")) + int(input("total Maquinaria: "))
print("COTOS INDIRECTOS")
indirect = int(input("Costos Administrativos: ")) + int(input("Costos de diseño y arquitectura: ")) + int(input("Costos de licencia: "))

costo_obra(direct, indirect)
