import random

# Define a deck of cards. In blackjack, Jacks, Queens, and Kings are all worth 10.
# Aces can be worth 11 or 1, depending on the hand. This list represents a standard deck of 52 cards.
DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4


# Function to draw a card from the deck
def draw_card(deck, infinite=True):
    # If infinite is True, draw a card without removing it from the deck
    # This simulates an infinite deck scenario, where the probability of drawing any card is always the same
    if infinite:
        return random.choice(DECK)
    else:
        # If infinite is False, draw a card and remove it from the deck
        # This simulates a realistic scenario where the deck gets smaller as cards are drawn
        card = random.choice(deck)
        deck.remove(card)
        return card


# Function to calculate the value of a hand in blackjack
def hand_value(hand):
    # Sum the values of all cards in the hand
    value = sum(hand)
    # Count the number of aces in the hand
    aces = hand.count(11)

    # While the total value exceeds 21 and there are aces in the hand
    # Convert some aces from 11 to 1 (by subtracting 10 from total value)
    # This is done to prevent busting (going over 21)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

