#Crea una función que calcule la tasa de rotación de empleados de una empresa.
#FORMULA: R=S/((I+F))X100
def rotationRate(retired, initial, final):
    rate = 0
    rate = retired / ((initial+final)/2) * 100
    print("The actual staff turn over rate is: ", rate,"%")

retired = int(input("Please enter the number of retired personnel: "))
initial = int(input("Please enter the intial staff number: "))
final = int(input("Please enter the final staff number: "))

rotationRate(retired, initial, final)
