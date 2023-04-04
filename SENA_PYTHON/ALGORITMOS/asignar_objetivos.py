docentes = [
    "Juan Carlos",
    "Martha Ramirez",
    "Pedro Sanchez"
]

objetivos = [
    "1. Fortalecer la participación de los estudiantes",
    "2. Mejorar el rendimiento academico",
    "3. Desarollo de competencias",
    "4. Mejorar la tención de los estudiantes"
]



(print("""Please select the teacher
1. Juan carlos
2. Martha Ramirez
3. Pedro Sanchez 
"""))

select = int(input())

if  select == 1:
    print("You've selected: ", docentes[0])
elif select == 2:
    print("You've selected: ", docentes[1])
elif select == 3 :
    print("You've selected: ", docentes[2])

print(
    """Please Select the Option you want to execute: 
    1. Asignar Objetivos de desempeño
    2. Consultar objetivos de desempeño
    3. Enviar mensaje"""
)

select2 = int(input())


if select2 == 1:
    print("Which Option you want to asign: ")
    for a in objetivos:
        print(a)
else:
    print("This option is currently unavailable")
    
select3 = int(input())

if select3 == 1:
    print("You've Selected: ", objetivos[0])


#Falta seleccionar los demas objetivos con el if y elif, y confirmar asignar o cancelar.