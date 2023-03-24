#Calculadora básica
numero1 = (int(input("Ingrese el primer numero")))
numero2 = (int(input("Ingrese el segundo numero ")))

seleccion=0

print("""Que opcion deseas realizar?\n 
      1) Sumar los numeros\n
      2) Restar los numeros\n
      3) Multiplicar los numeros\n
      4) dividir los numeros\n""")

seleccion = int(input("Elije la operación por favor"))

if  seleccion == 1:
    print("La suma es: ", numero1 + numero2) 
elif seleccion == 2:
    print("La resta es: ", numero1 - numero2)
elif seleccion == 3:
    print("La multiplicación es: ", numero1 * numero2)
elif seleccion == 4:
    print("La division es: ", numero1 / numero2)








