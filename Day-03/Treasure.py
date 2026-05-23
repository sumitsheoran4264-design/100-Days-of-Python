print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[PYTHON]
*******************************************************************************''')
print("welcome to treasure island.")
print("your mission is to find the treasure.") 
left_or_right = input('you are at a cross road. where do you want to go? type "Left" or "Right". \n').lower()
if left_or_right == "left":
    swim_or_wait = input('you come to a lake.\nthere is an island in the middle of the lake.type "Wait" to wait for a boat.type "Swim" to swim across. \n').lower()
    if swim_or_wait == "wait":
        print("you wait for a boat and arrive at the island safely.")
        door = input("you arrive at the island unharmed.there is a house with 3 doors. one Red, one Yellow and one Blue. which colour do you choose? \n").lower()
        if door == "red":
            print("it's a room full of fire. game over.")
        elif door == "yellow":
            print("you found the treasure! you win!")
        elif door == "blue":
            print("you enter a room of beasts. game over.")
        else:
            print("you chose a door that doesn't exist. game over.")
    else:
        print("you decide to swim across the lake but there are crocodiles. game over.")
        
else:
    print("you fell into a hole. game over.")