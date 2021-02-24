from turtle import Screen, Turtle
from math import cos, sqrt, radians

turtle = Turtle()
screen = Screen()
turtle.speed(0)


i = 7                                                       # Arbitrary counter

while i > 0:                                                # For circles from 7 to 1 inclusive
    if i <= 3:                                              # But this is for the three inner circles, who have an exponential relationship r_n = r_{n-1}^2
        turtle.color('black', 'white')                      # This is a circle with a white color
        turtle.begin_fill()                                 # This is how we start a fill
        turtle.circle(2**(i-1)*5)                           # As the radius of the circle is exponential (x2 each time for first three) with arbitrary radisu 5
        turtle.end_fill()                                   # This is how we end a fill
        i -= 1                                              # We drew one circle, so remove 1 from counter

        if i == 0:                                          # To prevent from obtaining -1 and an extra circle
            break

        turtle.color('white', 'black')                      # For black circles
        turtle.begin_fill()                                 
        turtle.circle(2**(i-1)*5)
        turtle.end_fill()                                    
        i -= 1                                               

    if i > 4:                                               # Only the 4 circles outside have a linear relationship of 1.5x radois
        turtle.color('black', 'white')
        turtle.begin_fill()
        turtle.circle((i-1)*2*5)                            # Linear relationship
        turtle.end_fill()
        i -= 1

    if i > 3:                                               # There is a set number of black circles
        turtle.color('white', 'black')                      
        turtle.begin_fill()                                 
        turtle.circle((i-1)*2*5)
        turtle.end_fill()                                   
        i -= 1                                              

# This part is for the non-central circles
# Definition of variables r = radius, h = counter, ratio = radius ratio, angle = angle between each circle. Could be tweaked a bit
# Ever penup and pendown is to precent tracing lines when moving the "pen"
r = 60
h = 0
ratio = 1/1.4
angle = 35

turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.circle(60)                                           # Initial circle start                                          
turtle.left(90)
turtle.penup()   
turtle.forward(r)
turtle.pendown() 



turtle.penup()
turtle.right(120)                                           # Right side initial setup
turtle.forward(r*(ratio)**h)                                # This is the initial circle, so r = r
turtle.pendown()

while h < 6:
    turtle.right(90)
    turtle.circle(r*(ratio)**(h+1))
    turtle.left(90)
    turtle.penup()
    turtle.forward(r*(ratio)**(h+1))
    turtle.right(angle-h*3)
    turtle.forward(r*(ratio)**(h+1))
    turtle.pendown()
    h += 1

h = 0                                                       # We reset the counter in order to not declare a new variable

turtle.penup()
turtle.goto(0,150)                                          # Where the circle upper middle circle starts
turtle.setheading(90)
turtle.forward(r)

turtle.left(120)                                            # Left side initial setup
turtle.forward(r)                                           # Goes forward by radius size
turtle.pendown()

while h < 6:
    turtle.right(90)                                        # Turns 90 deg in order to draw circle in right direction
    turtle.circle(r*(ratio)**(h+1))                         # Draw the circle with variable size
    turtle.left(90)                                         # Point outwards parallel to the radius
    turtle.penup()
    turtle.forward(r*(ratio)**(h+1))                        # Go forward, same size as radius
    turtle.left(angle-h*3)                                  # Then turn with angle
    turtle.forward(r*(ratio)**(h+1))                        # Go again (from edge to center to edge)
    turtle.pendown()
    h += 1                                                  # We loop here

screen.mainloop()