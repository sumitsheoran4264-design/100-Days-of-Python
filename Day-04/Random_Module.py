# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 8 #most useful for generating random numbers between 0 and 1. if you want to generate a random number between 0 and 8, you can multiply the result by 8.
# print(random_float)


# random_float = random.uniform(1, 10)
# print(f"{random_float:.2f}") #.2f means 2 decimal places ex - 0.00


import random


r = random.randint(0, 1)
if r == 0:
    print("Heads")
else:
    print("Tails")