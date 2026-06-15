import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','#','$','%','&','(',')','*','+'] 

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols =int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many numbers you like?\n"))


#easy level
password =""
for charcter in range(0,nr_letters):
    password += random.choice(letters)

for charcter in range(0,nr_number):
    password += random.choice(numbers)

for charcter in range(0,nr_symbols):
    password += random.choice(symbols)

print(f"Your password is", password)















#hard level
# password_list =[]
# for charcter in range(0,nr_letters):
#     password_list.append(random.choice(letters))

# for charcter in range(0,nr_number):
#     password_list.append(random.choice(numbers))

# for charcter in range(0,nr_symbols):
#     password_list.append(random.choice(symbols))

# print(password_list) #without shuffle
# random.shuffle(password_list)
# print(password_list) #with random shuffle

# password = ""
# for charcter in password_list:
#     password += charcter

# print(f"Your password is: {password}")