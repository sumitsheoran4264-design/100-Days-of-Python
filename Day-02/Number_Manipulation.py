bmi = 84 / 1.65 ** 2
print(bmi) # Output: 30.86505190311416
print(int(bmi)) # Output: 30
print(round(bmi)) # Output: 31  #The round() function rounds the number to the nearest integer. If the decimal part is 0.5 or higher, it rounds up; otherwise, it rounds down.
print(round(bmi, 3)) # Output: 30.865 #The round() function can also take a second argument that specifies the number of decimal places to round to. In this case, it rounds the BMI value to 3 decimal places.



#f strings
name = "Sumit"
age = 18
print(f"he is {name} and his age is {age}")# Output: he is Sumit and his age is 18.