friends = ["amit", "sachin", "rohit", "virat", "dhoni", "yuvraj"]
import random

#1st way
print(random.choice(friends)) 

#2nd way
print(friends[random.randint(0, len(friends) - 1)]) # random.randint() is used to generate a random integer between the specified range. In this case, it generates a random index between 0 and the length of the friends list minus 1 (since list indices start at 0). The generated index is then used to access a random friend from the list.

