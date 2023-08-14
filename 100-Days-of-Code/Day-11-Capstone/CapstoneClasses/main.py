from player_class import Player
from deck_class import Deck

def main():
    player = Player("Player")
    dealer = Player("Dealer")
    deck = Deck(4)
    deck.shuffle()

    for _ in range(2):
        player.draw_card(deck.draw())
        dealer.draw_card(deck.draw())
 
    # Convert the list of cards to a formatted string
    player_hand = ", ".join(player.show_hand())

    print(f"{player.name} hand: {player.get_hand_value(deck)}")
    print(f"{dealer.name} hand: {dealer.show_hand()[0]}, ?")
    #print the sum of the player's hand
    print(f"{player.name} hand value: {player.get_hand_value(deck)}")


    # Rest of your game logic...

if __name__ == "__main__":
    main()
