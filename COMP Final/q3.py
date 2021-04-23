def check_pattern(sentence, pattern):
    pattern = pattern.lower()                   # Normalize the sentence and pattern by making them lowercase
    sentence = sentence.lower() 
    length = len(sentence)                      # We only want to find the length once
    firstLetter = pattern[0]                    # Simply attributing first to avoid accessingn the pattern multiple times
    secondLetter = pattern[2]
    blankLetters = int(pattern[1])

    counter = 0                                 # Counter to remember which index we are at
    for letter in sentence:
        counter += 1
        if letter == firstLetter:               # If the first letter is contained somewhere in the sentence,
            if sentence[counter + blankLetters] == secondLetter:    # check if the second letter is x position after, where x is the number of spaces we skip
                return True                     # If this is the case, then we can return True and break out of the loop
        if counter == (length - blankLetters):  # In case the counter reaches length - blankLetters and hasn't found the pattern, we can safely escape because
            return False                        # there is no way for a x length pattern to exist in a x-1 series of letters. Return False


state = check_pattern("something", "o1e")       # State is defined as True or False
print(state)