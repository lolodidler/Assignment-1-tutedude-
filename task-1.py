#asking user for input of two numbers

def result(num1 = float(input("Enter first number: ")), num2 = float(input("Enter second number: "))):
    #adding the two numbers
    addition = num1 + num2

    #subtractring the two numbers
    subtraction = num1 - num2

    #multiplying the two numbers
    multiplication = num1 * num2   

    #dividing the two numbers
    division = num1 / num2

    #printing the results, using the %f formater to display as float
    print("Adding the two numbers gives: %f" % addition)
    print("Subtracting the two numbers gives: %f" % subtraction)
    print("Multiplying the two numbers gives: %f" % multiplication)
    print("Dividing the two numbers gives: %f" % division)

#calling the function
result()