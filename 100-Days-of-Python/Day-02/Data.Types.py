print("Sumit"[0])  # Output: 'S'
print("Sumit"[1])  # Output: 'u'    
print("Sumit"[2])  # Output: 'm'
print("Sumit"[3])  # Output: 'i'        
print("Sumit"[4])  # Output: 't'
print("Sumit"[0:5])  # Output: 'Sumit'



#string concatenation 

#Integer Whole Number
print(123+123) # Output: 246
      
#Float Decimal Number
print(3.14 + 2.71) # Output: 5.85

#Larger Integer
print(1234_56789) # Output: 123456789
print(type(1234_56789)) # Output: <class 'int'>

a="Sumit"
b=22
c=3.14
d=True
print(type(a)) # Output: <class 'str'>
print(type(b)) # Output: <class 'int'>
print(type(c)) # Output: <class 'float'>
print(type(d)) # Output: <class 'bool'>
print("Number of letter in your name is: " + str(len(input("Enter your name: ")))) # Output: Number of letter in your name is:  5 (if input is 'Sumit')
  

name_of_The_user  = input("Enter your name: ")# Output: (if input is 'Sumit') Enter your name: Sumit
length_of_name = len(name_of_The_user) # Output: (if input is 'Sumit') 5

print (type("Number of letter in your name is: "))# Output: <class 'str'>
print (type(length_of_name))# Output: <class 'int'> 

print("Number of letter in your name is: " + str(length_of_name))# Output: Number of letter in your name is: 5 (if input is 'Sumit')