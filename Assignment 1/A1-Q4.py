name = str(input("Please enter your name: ")) #These two lines ask for password and name, then store them in variable
pw = str(input("Please enter a password: "))

print("Welcome", name) # Prints name

pwLength = len(pw) #Checks the length of the password
pwList = list(pw) #Lists each character of the string in a single array

print("Your password has " + str(pwLength) + " characters.") #Prints the number of characters in the string

if (pwLength < 8): #If the length of the password is smaller than 8, print the following message
    print("Your password has less than 8 characters. We recommend at least 8 characters for the safety of your account.")

print("This is your obfuscated password: " + str(pwList[0]) + "#"*(pwLength-2) + str(pwList[pwLength-1]))

        #This command is special. It takes the first character of the array of characters (hence index 0)
        #Then it takes the length of the password-2, because you expose the first and last characters of the password
        #times #, in order to obfuscate
        #Finally, it takes the last index (length - 1) and prints the character associated to it, which is the last
        #Character of the password