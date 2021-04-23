#Q7
class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def checkHealth(self):
        bmi = self.weight/(self.height**2)
        if bmi > 18.5 and bmi < 24.9:
            print("Healthy")
        elif bmi >= 24.9:
            print("Overweight")
        else:
            print("So so")

BMI(70,1.7).checkHealth()

#Q8
a = int(input("Bruh"))
b = int(input("Bruh"))
c = int(input("Bruh"))

def isRightTriangle(a,b,c):
    return a**2+b**2==c**2

print(isRightTriangle(a,b,c))

#Q9
validNumbers = []
for i in range(1000,2001):
    if i % 3 == 0 and i % 5 != 0:
        validNumbers.append(i)

validNumbersString = " - ".join(str(i) for i in validNumbers)
print(validNumbersString)

#Q10
class Abreviate:
    def __init__(self,sentence):
        self.sentence = sentence
    def shorten(self):
        string_ = self.sentence.split()
        list_ = [string_[i][0] for i in range(0,len(string_))]
        return "".join(str(j) for j in list_).upper()

ab = Abreviate("Hello dear Comp208 class")
shortened = ab.shorten()
print(shortened)

#Q11
def gradeSystem(input):  # I am forced to use this because a list comprehension cannot have more than one if and one else clause, while the question asks for 3 if/else statements
    if input > 60:
        return "Pass"
    elif input < 40:
        return "Fail"
    else:
        return "Average"

def transform(inputDict):
    return [gradeSystem(inputDict[i]) for i in inputDict]

print(transform({"Steve":75, "Aron":34, "Jessica":45}))