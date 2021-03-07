from math import pi

shape = str(input("Which shape are you interested in? \nPossibilities: sphere, triangle, rectangle, circle: "))
shape = str.lower(shape) #Makes sure that the input is in lowercase so that it can be compared later

# This program could have used a switch statement, but for assignment 1 if statements will have to do

if (shape == "sphere"):
    radius = float(input("Please enter the value of the radius: ")) #Asks for input, turns it into a float
    area = 4*pi*radius**2
    print("The area of a sphere of radius " + str(radius) + "​ is " + str(area)) #Outputs answer

elif (shape == "triangle"):
    base = float(input("Please enter the value of the base: ")) #Asks for input, turns it into a float
    height = float(input("Please enter the value of the height: ")) #Asks for input, turns it into a float
    area = base*height/2
    print("The area of a triangle of base " + str(base) + "​ and height " + str(height) + " is " + str(area)) #Outputs answer

elif (shape == "rectangle"):
    base = float(input("Please enter the value of the base: ")) #Asks for input, turns it into a float
    height = float(input("Please enter the value of the height: ")) #Asks for input, turns it into a float
    area = base*height
    print("The area of a rectangle of base " + str(base) + "​ and height " + str(height) + " is " + str(area)) #Outputs answer

elif (shape == "circle"): 
    radius = float(input("Please enter the value of the radius: ")) #Asks for input, turns it into a float
    area = pi*radius**2
    print("The area of a circle of radius " + str(radius) + "​ is " + str(area)) #Outputs answer

else: #Catches outliers
    print("You have entered an invalid shape name. Only the following shapes aresupported: sphere, triangle, rectangle or circle.")

