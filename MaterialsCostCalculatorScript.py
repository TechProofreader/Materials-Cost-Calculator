# Author: Ryan Reyes (github.com/TechProofreader)
# Program Name: Materials Calculator Script
# Version: 1.0

import time

print("Note: for all questions, please only input numbers. Leave out any symbols such as $, %, etc.")

time.sleep(2)

print("What are the dimensions of your project?")

def errorFunction(lit): # the 'lit' call tells the computer to just use the literal string from the input
    while True:
        try:
            x = float(input(lit )) # an if statement is not needed here because if the program 
            break                  # can't convert the input to float, it will throw errors 
        except ValueError:
            print("Please only enter numbers.")
    return x

length=errorFunction("Length: ") # the 'lit' call will literally pass through whatever the user
                                # inputs here and all other places where user input is passed
print("by")                     #  through the errorFunction()

width=errorFunction("Width: ")

area = abs(round(length*width, 2))

print("The total area of your project is", str(area)+".")

costPerSqFt = abs(errorFunction('What is the cost of the materials you plan on using (per sq-ft, for example)?:' ))

beforeTaxCost = round(costPerSqFt*area, 2)

print("The total cost of materials before tax is:", str(beforeTaxCost)+".")
time.sleep(1)
print("If you know your sales tax rate and would also like to know the total cost of materials plus tax, please type \'yes\', otherwise please type \'no\'.")

while True:
    try:
        list = ["yes", "no"]
        salesTaxYesNo = input()
        salesTaxYesNo = salesTaxYesNo.lower()
        if salesTaxYesNo not in list:
            raise ValueError
        break
    except ValueError:
        print("Please only type \'yes\' or \'no\'.")

if salesTaxYesNo == "yes":

    while True:
        try:
            tax = abs(float(input("Please input your sales tax in percentage form without the \'%\' symbol:")))
            if tax is float(tax):
                taxToPercentage = (tax / 100)
                print("The total cost of your project is:", str((round(costPerSqFt*area*(1+(taxToPercentage)), 2)))+".")
                print("Thank You for using my materials cost calculator tool, good luck with your project!")
            if tax is not float(tax):
                raise ValueError
            break
        except ValueError:
            print("Please only enter numbers")

elif salesTaxYesNo == "no":
    print("Thank You for using my materials cost calculator tool, good luck with your project!")

exit
