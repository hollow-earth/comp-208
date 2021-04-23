def shift_characters(word, number, direction):
    errorState = False
    direction = direction.lower()

    if word == "":                                  # If word is empty
        print("Empty word, try again")
        errorState = True                           # Error flag to prevent the program from executing at line 20
    
    if len(str(word)) <= 1 and errorState == False: # Prevent the program from executing if the program has a single letter (useless)
        print("Word is too short, try again")
        errorState = True

    if type(number) is not int:                     # Catches errors for the use of anything other thank integers as second argument
        print("Number is not an integer, try again")
        errorState = True
    
    if (direction.lower() != "left" and direction.lower() != "right"):  # If direction is neither left nor right, call an error
        print("Direction is invalid, try again")
        errorState = True

    if errorState == False:
        if direction == "left":
            beginning = word[number:]               # Pick the first n letters (n=number)
            ending = word [:number]                 # Pick the rest of the letters
            result = beginning + ending             # Add them together, equivalent to a switch
        elif direction == "right":
            beginning = word[-number:]              # Pick the last n letters
            ending = word[:-number]                 # Pick the rest of the letters
            result = beginning + ending             # Add them together, equivalent to a switch
    print(result)

shift_characters("Galadriel", 1, "right")