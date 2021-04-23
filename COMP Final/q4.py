import numpy as np
import matplotlib.pyplot as plt

def f(x):                                                       # We define the function first
    return np.sin(x) 

class Bisection:
    def __init__(self, epsilon, intervalBegin, intervalEnd, function):
        self.epsilon = epsilon
        self.intervalBegin = intervalBegin                      # This is a variable which determins x1 in (x1, x2) interval
        self.intervalEnd = intervalEnd                          # This is x2
        self.originalBegin = intervalBegin                      # This does not change, used as reference
        self.originalEnd = intervalEnd                          # Same
        self.function = function
    
    def __str__(self):
        return str(self.result)                                 # To be able to print the actual result instead of the memory location
    
    def solve(self):
        f1, f2 = self.function(self.intervalBegin), self.function(self.intervalEnd) # Declare these two variables
        if f1 == 0:                                             # If either f1 or f2 are 0, then we have our answer
            self.result = self.intervalBegin
            return                                              # Used to exit the function
        if f2 == 0:
            self.result = self.intervalEnd
            return
        if 0 < f1 * f2:                                         # If there isn't one negative and one positive value, then the bisection method does not work for that interval
            raise ValueError("The root cannot be found within this interval.")

        while (self.intervalEnd-self.intervalBegin) > self.epsilon:     # Keep going until we reach the desired accuracy
            a = 0.5 * (self.intervalBegin + self.intervalEnd)   # We find the center point of those two
            f_of_a = f(a)                                       # Evaluate that point

            if f_of_a == 0:                                     # If that point is 0, there's our answer
                self.result = a
                break
            elif 0 > f2 * f_of_a:                               # This means the sign between midpoint and intervalEnd has changed, thus we keep going this way
                self.intervalBegin, f1 = a, f_of_a
            else:                                               # This means the sign between midpoint and intervalBegin has changed, thus we keep going this way
                self.intervalEnd, f2 = a, f_of_a
        self.result = (self.intervalBegin + self.intervalEnd)/2 # If the interval is small enough, we return the midpoint (the answer)
    
    def graphit(self):
        plt.title("Graph of the Function f")                    # Give it a title and then labels
        plt.xlabel("x")
        plt.ylabel("y")
        x = np.linspace(self.originalBegin, self.originalEnd, int((self.originalEnd - self.originalBegin)*100)) # Plot for values in interval, then plot for every 0.01
        y = f(x)                                                # Compute the function
        plt.xlim(self.originalBegin, self.originalEnd)          # Set the graph limits
        plt.plot(x,y)                                           # Plot, then show
        plt.show()

b = Bisection(0.00001, 1, 99, f)
b.solve()
print(b)
b.graphit()