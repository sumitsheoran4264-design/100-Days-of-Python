#Blackjack
import random
#step-1 create a function for return rondom card from the list of cards.
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card()) 

