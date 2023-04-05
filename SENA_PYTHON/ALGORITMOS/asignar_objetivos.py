#Define lists variables
docentes = [
    "1. Juan Carlos",
    "2. Martha Ramirez",
    "3. Pedro Sanchez"
]

objetivos = [
    "1. Fortalecer la participación de los estudiantes",
    "2. Mejorar el rendimiento academico",
    "3. Desarollo de competencias",
    "4. Mejorar la tención de los estudiantes"
]

requires = [
    "1. Asign to all courses",
    "2. Set time "
]


#Ask user to select a teacher from the list 
(print("Please select the teacher: "))
for d in docentes:
    print(d)

#Input number of teacher from lists
select_docente = int(input())

#Conditional to validate which teacher is selected from the lists
if  select_docente == 1:
    print("You've selected: ", docentes[0])
elif select_docente == 2:
    print("You've selected: ", docentes[1])
elif select_docente == 3 :
    print("You've selected: ", docentes[2])

#TODO : Start to manage errors at the moment to select 

#Options that user will select (In this case: 1. Asignar Objetivos de desempeño)
print(
    """Please Select the Option you want to execute: 
    1. Asignar Objetivos de desempeño
    2. Consultar objetivos de desempeño
    3. Enviar mensaje"""
)

#User inputs the option
select_option = int(input())

# Conditional to validate which option was selected by the user and an array will show from the array objetivos[]
if select_option == 1:
    print("Which Option you want to asign: ")
    for o in objetivos:
        print(o)
else:
    print("This option is currently unavailable")

# User inputs the number of the objetivos[] from the lists   
select_objetivos = int(input())

# Conditional validates which objetivo is selected from the list objetivos[]
if select_objetivos == 1:
    print("You've Selected: ", objetivos[0])
elif select_objetivos == 2:
    print("You've selected: ", objetivos[1])
elif select_objetivos == 3:
    print("You've selected: ", objetivos[2])
elif select_objetivos == 4:
    print("You've selected: ", objetivos[3])

# Print in console another lists the user must select from requires[] and an a for to traverse the array
print(""" Please select the requirements for this task""")
for r in requires : 
    print(r)

# User inputs the 2 options from the array
select_req1 = int(input())
select_req2 = int(input())

# Conditional to validate the two requirements must be selected
if select_req1 == 1 and len(requires) and select_req2 == 2 and len(requires):
    print("""You have selected all requirements:
    Please confirm:  
    1. Submit
    2. Cancel
    """)

# An inut to submit or cancel 
submit = int(input())

if submit == 1:
    print("You have asigned this Tasks Succesfully !")
elif submit == 2:
    print("This task was canceled!")






