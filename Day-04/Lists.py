India = ["Delhi", "Mumbai", "Bangalore", "Haryana", "Punjab"] # List of cities in India

import random
random_city = random.choice(India) # random.choice() is used to select a random item from a list
print(random_city)

random.shuffle(India) #random.shuffle is for mix the Lists
print(India)
print("Delhi"[0]) # to print the first letter of the word "Delhi"
