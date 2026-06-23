#Hiher lower
import random
from art import logo, vs

from game_data import data
# step -01 (art)
print(logo)
score = 0

# make the game repetable.
game_should_continue = True
account_b = random.choice(data)



while game_should_continue:
    def format_data(account):
        '''Format the data into printable format.'''
        account_name = account["name"]
        account_descrpition = account["description"]
        account_country = account["country"]
        return (f"{account_name}, {account_descrpition}, from {account_country}")

    def check_answer(user_guess, a_followers, b_followers):
        """Take the user guess and follower counts and return if they got it right """
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess == "b"
        

    # step 02 - genrate a rondom account from the game data
    # 
    # # making account at position b become the next account at position A..
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # format the account data into printable format. 
    account_1 = format_data(account_a)
    account_2 = format_data(account_b)


    print(f"Compare A: {account_1}.")

    print(vs)

    print(f"Against B: {account_2}.")

    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    # clear the screen 
    print("\n" * 100)
    print(logo)
    ## get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ### give user feedback on their guess
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! current score: {score} ")
    else:
        print(f"sorry that's wrong. Final score: {score}")
        game_should_continue = False




