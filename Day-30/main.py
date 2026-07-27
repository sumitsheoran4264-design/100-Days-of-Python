# #name error
# a = 0 
# print(b)

# #syntax error
# b = 0
# print(b


# # Type error
# a = [3, 5, 8]
# print(a["boss"])


# # index error
# a = [1, 3, 5, 10]
# print(a[4])

# #key error
# car = {"BMW": (22, 22, "22")}
# print(car["Mustang"])

# #File not found error
# with open("game.txt") as game_data:
#     game = game_data.read()



#----------------------------------------#
#=========== Handling errors ============#
#----------------------------------------#

# try :
#     files = open("art.txt")
#     a = {"JAAT": "SHEORAN"}
#     print(a)
# except FileNotFoundError:
#     print("There was an error")

# finally:
#     raise TypeError("This is an error that I made up. ")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# bmi = weight / height ** 2

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
# print(bmi)




# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruits pie")
#     else:
#         print(fruit + " pie")

# make_pie(0)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    return total_likes


print(count_likes(facebook_posts))



 