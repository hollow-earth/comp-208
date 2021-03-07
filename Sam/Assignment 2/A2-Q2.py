from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()

#######################
### From question 1 ###
#######################

def getGrowth(population_year_zero, rate, immigration_per_year, nbr_of_years):
    if population_year_zero < 0 or nbr_of_years < 1:                                # If these essential values are non-valid, raise an exception
        raise Exception("One of your values is incorrect. Try again.")

    resultList = [population_year_zero]                                             # First index is year 0 population

    for i in range(1,nbr_of_years+1):                                               # For years 1 to max years inclusive:
        result = (1+rate)*resultList[i-1]+immigration_per_year                      # We do the calculation
        resultList.append(result)                                                   # We add the result to the next index in the list
    
    resultList.pop(0)                                                               # We remove year 0
    return resultList

#######################
#######################
#######################

def graphGrowth(growth_table):
    for i in range(0, len(growth_table)):
        turtle.penup()                                                              # We don't want lines, so the pen is "up"
        turtle.goto(i*100,0)                                                        # We multiply the x coordinate by 100 because otherwise it's not very noticeable and then go there
        turtle.pendown()                                                            # We start drawing after going to the x coordinate
        turtle.circle(growth_table[i]/100)                                          # We make a circle the radius the size of results/100 (for scaling)

p0 = float(input("Input the initial population at year zero: "))
rate = float(input("Enter the rate: "))
immigration = float(input("Enter the immigration per year: "))
years = int(input("Input the number of years as an integer: "))

resultList = getGrowth(p0, rate, immigration, years)                                # Calling the method

graphGrowth(resultList)

screen.mainloop()