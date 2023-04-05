# ALGORITM Consultar objetivos:

#IMPORTS
import sys

#Credentials
username = "Jhonatan"
password = "abc123"

docentes = [
    "1. Juan Carlos",
    "2. Martha Ramirez",
    "3. Pedro Sanchez"
]

options = [
    "1. Asignar Objetivos de desempeño",
    "2. Consultar objetivos de desempeño",
    "3. Enviar mensaje"
]

objetivos = [
    "\n1. Fortalecer la participación de los estudiantes",
    "2. Mejorar el rendimiento academico",
    "3. Desarollo de competencias",
    "4. Mejorar la tención de los estudiantes"
]


print("""Please enter your credentials""")

try:
    enter_username = input("\nUsername: ")
    enter_password = input("\nPassword: ")
    if enter_username == username and enter_password == password:
        print("\nLogged in Succesful!")
    else: 
        raise ValueError("\nInvalid credentials, Try again!")

except KeyboardInterrupt:
    print("\nlogin process canceled")
except ValueError as err:
    print(err)
    sys.exit()
    

print("\nSelect Teacher's profile: ")
for d in docentes:
    print(d)

try:
    select_docente = int(input())
    if select_docente == 1:
        print("Teacher: ", docentes[0])
    elif select_docente == 2:
        print("Teacher: ",docentes[1])
    elif select_docente == 3:
        print("Teacher: ",docentes[2])
    else:
        raise ValueError("\nInvalid Selection, Try again!")
    
except KeyboardInterrupt:
    print("\nSelection process Canceled")
except ValueError as err:
    print(err)
    sys.exit()

# Check results
print("Select the task you want to request: ")
for ob in objetivos:
    print(ob)

try:
    select_obj = int(input())
    if select_obj == 1:
        print(objetivos[0], ":", "\nThis task is 80% Completed")
    elif select_obj == 2:
        print(objetivos[1], ":", "\nThis task is 50% Completed")
    elif select_obj == 3:
        print(objetivos[2], ":", "\nThis task is 100% Completed")
    elif select_obj == 4:
        print(objetivos[3], ":", "\nThis task is 0% Completed")
    else:
        raise ValueError("\nInvalid Selection, Try again!")
except KeyboardInterrupt:
    print("\nProcess cancelled")
except ValueError as err:
    print(err)
    sys.exit()


