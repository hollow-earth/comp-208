print("Welcome to Comp 208 time converter. \n")                                             # Prints welcome message
timeInput = int(input("Please enter the time to convert (hours only without minutes): "))   # Asks for user input, then converts it to an integer for calculations.

if (timeInput >= 0 and timeInput <= 12): # Checks if the number is in the interval [0,12]
    print("You have entered " + str(timeInput) + " in 24h mode. The equivalent in 12h mode is: " + str(timeInput).zfill(2))

elif (timeInput >= 13 and timeInput <= 23): # Checks if the number is in the interval [13,23]
    print("You have entered " + str(timeInput) + " in 24h mode. The equivalent in 12h mode is: " + str(timeInput - 12).zfill(2)) 
    
    # Prints the message, with the time. zfill(2) simply pads the final answer so that it always prints 2 characters,
    # even if the number is smaller than 10.

elif (timeInput < 0 or timeInput > 23): # Checks if the number is outside the interval (0,23), then prints the invalid message
    print("The number is invalid")