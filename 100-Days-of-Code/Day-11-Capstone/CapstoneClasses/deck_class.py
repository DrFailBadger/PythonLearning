import random

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        self.cards = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks] * num_decks

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            raise ValueError("Deck is empty!")
        return self.cards.pop()

    def get_card_value(self, card):
        rank = card[:-1]  # Extract the rank from the card string
        return self.card_values[rank]
