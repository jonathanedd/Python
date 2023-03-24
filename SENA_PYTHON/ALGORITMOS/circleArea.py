def circleArea(diam):
    pi = 3.1416
    perimeter = diam * pi

    print("The perimiter is: ", perimeter)
    rad = diam / 2 
    print("The radios is :", rad)

    totalArea = perimeter * rad / 2 
    print("The total circle area is: ", totalArea)


diam = int(input("Please enter the circle diameter value"))    
circleArea(diam)