#Keep in mind this code could be a lot more efficient if not limited by the usage of multiple functions

alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
countWordDict =  dict()
characterDict = dict()

def textAnalyser(inputString):
    if inputString != "" and inputString != " ":                    # If text isn't empty, proceed
        numberWords(inputString)
        wordCount(textString)
        characterCount(textString)
        specialCharacterCount(textString)
    else:
        print("Text is empty.")

def numberWords(inputString):
    lowercase = inputString.lower() + " "                           # Adding " " for the counting to work properly (closure for the last word)
    numberWordsInt = 0                                              # Initially 0 for obvious reasons
    contains_alpha = False                                          # Flag for detecting whether the sequence of chars is a word or not
    
    for char in lowercase:                                          # For every characted in the string
        if char in alphanumeric:                                    # If the character is alphanumeric, this automatically makes it a word until the next space
            contains_alpha = True                                   # Change flag to true
        elif char == " ":                                           # If it's a space, it's potentially a new word
            if contains_alpha == True:                              # However, to be a word it has to contain an alphanumeric character, hence this check
                numberWordsInt += 1                                 # Straightforward, if it's a new word then we add 1 to the word count
                contains_alpha = False                              # Reset the flag

    print("Number of words in the text: ", numberWordsInt)          #Print the number of words

def checkWord(inputWord):                                           # Could've used .isalphanum() but this may have been considered too advanced for the class
    word = inputWord.lower()
    contains_alpha = False

    for char in word:                                               # For every characted in the word being checkes
        if char in alphanumeric:                                    # If the character is alphanumeric, this automatically makes it a valid word
            contains_alpha = True
            break                                                   # As soon as there is a single alphanumeric character, it is indeed a word, thus we can prevent recursive checking

    return contains_alpha

def wordCount(inputString):
    splitArray = inputString.lower()                                # We make the string lowercase for checking
    splitArray = splitArray.split(" ")                             # We split words into different indices for a list 

    for i in range(0,len(splitArray)):                              # "For every word in this list"
        if checkWord(splitArray[i]) == True:                        # If it is a valid word
            if list(splitArray[i])[-1] not in alphanumeric:
                splitArray[i] = splitArray[i][:len(splitArray[i])-1]# This is to prevent words like class!, !class, and class to be counted as three separate words
            if list(splitArray[i])[0] not in alphanumeric:
                splitArray[i] = splitArray[i][1:]                   # Same as above, this one checks the first letter for non-alphanum characters
            if splitArray[i] not in countWordDict:                  # We initialize it in the dictionary if it doesn't exist
                countWordDict[splitArray[i]] = 1
            elif splitArray[i] in countWordDict:                    # If it exists in the dictionary, then we add 1
                countWordDict[splitArray[i]] += 1
                
    for i in countWordDict:                                         # For every word in the dictionary, we print the following line
        print("Number of times word \"", str(i), "\" is used:", countWordDict[i])

def characterCount(inputString):
    lowercase = inputString.lower()
    mostUsedLetters = []
    
    for char in lowercase:                                          # For every character in the string
        if char not in characterDict and char != (" " or ""):       # If it isn't a space, empty AND it is not in the dictionary, we inistialize it
            characterDict[char] = 1
        elif char in characterDict:                                 # If it exists in the dictionary, then we add 1
            characterDict[char] += 1

    mostUsed = max(characterDict.values())                          # We find the biggest char count
    
    for i in characterDict:                                         # For every key in the dictionary
        if characterDict[i] == mostUsed and (i in alphanumeric):    # If the key is equal to the biggest char count AND it is an alphanumeric character
            mostUsedLetters.append(i)                               # then we add it to the list

    if len(mostUsedLetters) == 1:                                   # Grammar
        print("Your most used letter was", mostUsedLetters, "with", mostUsed, "occurences.")
    elif len(mostUsedLetters) > 1:
        print("Your most used letters were", mostUsedLetters, "with", mostUsed, "occurences each.")
            
def specialCharacterCount(inputString):                             
    lowercase = inputString.lower()
    specialChar = []
    for char in lowercase:
        if char not in specialChar and char not in alphanumeric+" ":# If character is not already in the dictionary and is not alphanumeric or a space
            specialChar.append(char)                                # We add it to the list
    
    if len(specialChar) >= 1:                                       # Grammar
        print("Special characters detected in the text:", specialChar)
    else:
        print("No special characters were detected in the text.")

textString = input("Please input the text to be analyzed.\n")       # Input function
textAnalyser(textString)                                            # Initial function call