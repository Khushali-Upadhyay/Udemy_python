#Check which among the first two numbers is maximum
def findMaximum(firstNumber,secondNumber):
    if firstNumber > secondNumber:
        print("First number is greater")
        return firstNumber
    elif secondNumber > firstNumber:
        print("Second number is greater")
        return secondNumber
    else:
        print("Both the numbers are equal")
print("Enter the first number:")
firstNumber = int(input())
print("Enter the second number:")
secondNumber = int(input())
maximumNumber=findMaximum(firstNumber,secondNumber)
print("Maximum number = {}".format(maximumNumber))
