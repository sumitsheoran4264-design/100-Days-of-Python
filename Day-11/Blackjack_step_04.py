import random

#step-1 create a function for return rondom card from the list of cards.
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(u_score, c_score):
        if u_score == c_score:
            return "Draw"
        elif c_score == 0:
            return "Lose, opponent has Blackjack"
        elif u_score == 0:
            return "You win with a Blackjack"
        elif u_score > 21:
            return "You went over. You lose "
        elif c_score > 21:
            return " Opppnent went over. You win"
        elif u_score > c_score:
            return "You win"
        else:
            "Opponent win"


    calculate_score(cards= user_cards)
    calculate_score(cards= computer_cards)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = (calculate_score(cards= user_cards))
        computer_score = (calculate_score(cards= computer_cards))
        print(f"Your card {user_cards} and the current score: {user_score}")
        print(f"Computer card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_anoter_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if draw_anoter_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score:{user_score}")
    print(f"Opponent's hand: {computer_cards}, final score:{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 100)
    play_game()

    