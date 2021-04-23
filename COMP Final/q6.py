def getXandYintercepts(p1, p2):
    if p1 == p2:
        print("The two points are the same. There is no line, hence no intercepts.")

    elif p1[0] == p2[0]:                # Vertical slope
        x_intercept = p2[0]             # Assign the x value of either p1 or p2
        y_intercept = "non-existent"
    
    elif p1[1] == p2[1]:                # Horizontal slope
        x_intercept = "non-existent"
        y_intercept = p2[1]             # Assign the y value of either p1 or p2
    
    else:
        m = (p2[1]-p1[1])/(p2[0]-p1[0]) # Self explanatory, finding slope, then constant
        c = p2[1] - m * p2[0]
        x_intercept = -c/m              # Finding the intercept according to 0 = mx + c -> x = -c/m
        y_intercept = c                 # Finding the intercept according to y = c

    if p1 != p2:                        # To prevent an error from occuring if p1 == p2, as neither x or y intercepts have been defined
        print("The x intercept is {0}, the y intercept is {1}".format(x_intercept, y_intercept))        # Print results

getXandYintercepts((5, 2), (7, 2))