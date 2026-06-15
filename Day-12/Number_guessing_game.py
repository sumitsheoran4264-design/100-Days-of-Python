import random
#step 01 - a fuction for check answer 
def check_answer(user_guess, Actual_answer):
        """Check answer against guess"""
        if user_guess > Actual_answer:
            print("Too high")    
        elif user_guess < Actual_answer:
            print("Too low")
        else:
            print(f"You got it, the answer was {Actual_answer}.")


easy_level_attempts = 10
hard_level_attempts = 5

#step 02 -a function for difficulty (easy or hard)
def set_difficulty():
            
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_difficulty == 'easy':
        return easy_level_attempts
    else:
        return hard_level_attempts
    
            

def game():        
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 to 100.")
    answer = random.randint(1, 100)


    turns = set_difficulty() # if user choice easy turn = 10, otherwise turn = 5
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        turns -= 1
        

        check_answer(user_guess=guess, Actual_answer=answer) #check_answer()
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        
  

game()
