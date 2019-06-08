# Author: Ryan Reyes (github.com/TechProofreader)
# Program Name: Materials Calculator Script
# Version: 1.0
# License: MIT License
#
# Copyright (c) 2019 Ryan Reyes (github.com/TechProofreader)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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