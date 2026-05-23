print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Yes or No. ")
extra_cheese = input("Do you want extra cheese? Yes or No. ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed an invalid size.")


if pepperoni == "Yes":
     if size == "S":
         bill += 2
     else:
         bill += 3
  
if extra_cheese == "Yes":
    bill += 1

print(f"Your final bill is: ${bill}.")