#Función calculadora, se define la función con 4 parametros
def calculadora (sum, res, mult, div):
    
    #Se le piden dos valores al usuario
    num1 = int(input("Porfavor ingrese el primer numero"))
    num2 = int(input("Porfavor ingrese el segundo numero"))

    #asignación de variables a los parametros
    sum= num1 + num2
    res = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    
    #Seleccion inicializada en 0
    seleccion=0

    #Selección que hará el usuario
    print(""" Por favor selecione la operacion 
    1. para sumar
    2. para restar
    3. para multiplicar
    4. para dividir""")

    #Guardamos la seleccion del input en seleccion
    seleccion = int(input("Operacion: "))

    #La condicion que valida que tipo de operación ha seleccionado
    if seleccion == 1:
       print("La suma es: ", sum)
    elif seleccion == 2:
        print("La resta es: ", res)
    elif seleccion == 3:
        print("La multiplicación es: ", mult)
    elif seleccion == 4:
        print("La división es: ", div)
calculadora("suma", "Resta", "Multiplicación", "División")
#Se llama la función con los argumentos correspondientes
       

