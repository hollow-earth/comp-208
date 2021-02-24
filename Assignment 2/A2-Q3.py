def getGrowthRecursive(population_year_zero, rate, immigration_per_year, nbr_of_years):
    if population_year_zero < 0 or nbr_of_years < 1:                                # If these essential values are non-valid, raise an exception
        raise Exception("One of your values is incorrect. Try again.")

    result = population_year_zero                                                   # Because result is used recursively, we start by assigning it the value of p0
    i = 0
    
    while i < nbr_of_years:                                                         # While arbitrary variable i (counter) is smaller than the number of years
        result = (1+rate)*result+immigration_per_year                               # We do the calculation, taking result on the right hand side to be p-1
        i += 1
    return result                                                                   # We return it to line 17

p0 = float(input("Input the initial population at year zero: "))
rate = float(input("Enter the rate: "))
immigration = float(input("Enter the immigration per year: "))
years = int(input("Input the number of years as an integer: "))

growth_table = getGrowthRecursive(p0, rate, immigration, years)                     # Calling the method
print(growth_table)