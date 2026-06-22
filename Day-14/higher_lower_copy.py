from art import logo, vs
from game_data import data
import random
def format_data(account):
    account_name = account["name"]
    account_discr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, {account_discr}, {account_country}.")
def compare_followers(user_guess, account_a_followers, account_b_followes):
    if account_a_followers > account_b_followes:
        return user_guess == 'a'
    else: 
        user_guess == 'b'



score = 0
account_b = random.choice(data)
game_continue = True


while game_continue:
    print(logo)
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:", format_data(account_a))

    print(vs)

    print(f"Against B:", format_data(account_b))
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]



    guess = input("Who have more follower? Type 'A' or 'B': ").lower()

    print('\n' * 100)
    print(logo)

    is_correct = compare_followers(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You are right. your current score is: {score}.")
    else:
        game_continue = False
        print(f"Sorry you are wrong. your score is: {score}.")
        