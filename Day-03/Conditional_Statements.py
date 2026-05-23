print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120: 
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket are $5.") 
    elif age < 18:
        bill = 7
        print("Youth ticket are $7.")
    
    elif age >= 45 and age <= 55:
        bill = 0
        print("everything is going to be ok. have a free ride on us!")
    
    else:                          #when age >= 18
        bill = 12
        print("Adult ticket are $12.")
        

    wants_photo = input("Do you want a photo taken? yes or no. ")
    
    if wants_photo == "yes":
        
         bill += 3 
    
    print(f"your final bill is ${bill}")
else:                                      
    print("sorry, you have to grow taller before you can ride.")