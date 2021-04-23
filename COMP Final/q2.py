class Sorting:
    def __init__(self, algorithm):
        self.algorithm = algorithm
    
    def __str__(self):                                                      # Function for returning a string value instead of memory location
        returnString = " - ".join(str(i) for i in self.sortedList)          # We format the string such that it becomes a - b - ...
        return returnString

    def mySort(self, toSortList):
        length = len(toSortList)                                            # Equivalent to N 

        if self.algorithm == 1:                                             # If we choose selection sort
            for i in range(length):                                         # First we iterate through each number
                index = i
                for j in range(i+1, length):                                # Then we iterate the next number, for each number in i
                    if toSortList[index] >= toSortList[j]:                  # If that number is greater than the preceding number, we invert the indices
                        index = j
                tempVar = toSortList[i]                                     # We declare a temporary variable for changing the values
                toSortList[i] = toSortList[index]                           # First, assign the first and second numbers to be the same
                toSortList[index] = tempVar                                 # Then make the second number the bigger value, swap is complete. Now rinse and repeat
            self.sortedList = toSortList                                    # Return this variable to be used within the class

        elif self.algorithm == 2:                                           # If we choose insertion sort
            for i in range(1, length):                                      # For each element, starting with the second
                value = toSortList[i]                                       # We assign a temporary value
                j = i-1                                                     # We create a second index
                while j >= 0 and toSortList[j] > value:                     # If the previous number is greater than the current number, do the following
                    toSortList[j+1] = toSortList[j]                         # Assign the smaller number to become the bigger number
                    j -= 1
                toSortList[j+1] = value                                     # Then make the smaller number the preceding number
            self.sortedList = toSortList

        else:
            print("This value is invalid, choose 1 for selection sort, choose 2 for insertion sort")

s = Sorting(2)
s.mySort([2, 2, 2, 22, 11, 7,3,55,1254,4564,485])
print(s)