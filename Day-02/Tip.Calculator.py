print("Welcome to the tip Calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = bill + (bill * tip / 100)
per_person = total / people #This line calculates the amount each person should pay by dividing the total bill (including tip) by the number of people splitting the bill. The result is stored in the variable per_person.
print(f"Each person should pay: ${per_person:.2f}") #The :.2f format specifier formats the per_person value to 2 decimal places, ensuring that the output is displayed as a monetary amount with two digits after the decimal point. 
#end of code




