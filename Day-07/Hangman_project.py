import random
#Hangman project

print("Welcome to Hangman game!")
character= ["sumit", "amit", "hangman"]
random_word = random.choice(character)
print(f"Random word: {random_word}")
placeholder = ""
word_length = len(random_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder) # word length change with underscore _ _ _ _
lives = 6
game_over = False
correct_letter = []
while not game_over:
    guess_letter = input("Guess a letter: ").lower()

    display = ""

    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letter.append(guess_letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)
    if guess_letter not in random_word:
        lives -= 1
        if guess_letter == 0:
            game_over = True
            print("You lose")
    
    if "_" not in display:
        game_over = True
        print("You win")
