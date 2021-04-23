#import os

class FileManager:
    def __init__(self, filename):
        self.filePath = filename                                    # First, "load" the variable into the whole class

    def addText(self):
        self.file = open(self.filePath, "a")                        # Open in append mode, creates file if it doesn't exit, otherwise adds lines
        userInput = ""                                              # Declare variable
        print("Enter the sentence to be added to the file, or enter \"exit\" to escape the program.")
        while True:                                                 # Runs until "exit" is detected
            userInput = input()                                     # Asks for user input
            if userInput.lower() == "exit":                         # Breaks the loop when exit is detected
                break
            self.file.write(userInput+"\n")                         # Writes line to text file for each iteration
        self.file.close()                                           # Close file, unload from memory
    
    def readText(self):
        self.file = open(self.filePath, "r")                        # Open the file in reading mode
        print("These are the contents of the specified file:" + "\n" + self.file.read())    #Reads file contents, self explanatory
        self.file.close()

    def getLineNumber(self):
        self.file = open(self.filePath, "r")
        numberLines = len(self.file.readlines())                    # readlines() returns a list of lines, check the length of this list
        self.file.close()
        return numberLines                                          # We return the value so we can print it


f = FileManager("q1_text.txt")
f.addText()
f.readText()
number = f.getLineNumber()
print("Number of lines:", number)