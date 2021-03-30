from numpy import sqrt

#Gathers value of variables for calculation using input()
a = float(input("Please enter the value of \"a\": "))
b = float(input("Please enter the value of \"b\": "))
c = float(input("Please enter the value of \"c\": "))

if (b**2 - 4*a*c < 0): #Check if discriminant => 0. If not, says that the problem is invalid and exits
    print("The solutions are in the complex plane.")
    quit()

discriminant = sqrt(b**2 - 4*a*c) # In order to reduce the amount of calculations, the discriminant is only computed one time
sol_1 = (-b + discriminant)/(2*a)
sol_2 = (-b - discriminant)/(2*a)

# Prints both solutions, implying that the initial problem has a solution in the real plane
if (sol_1 != sol_2): #Checks that the two solutions are different. If not, there's only one real solution
    print("The first solution is: ​" + str(sol_1))
    print("The second solution is: ​" + str(sol_2))
elif (sol_1 == sol_2):
    print("The only solution is: ​" + str(sol_1))