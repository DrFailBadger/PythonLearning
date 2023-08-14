class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)
    
    def get_hand_value(self, deck):
        total_value = 0
        num_aces = 0

        for card in self.hand:
            card_value = deck.get_card_value(card)
            total_value += card_value
            if card_value == 11:
                num_aces += 1

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value
    
    def show_hand(self):
        return self.hand

    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def total(self, deck):
        total_value = 0
        num_aces = 0

        for card in self.cards:
            card_value = deck.get_card_value(card)
            total_value += card_value
            if card_value == 11:
                num_aces += 1

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value   
