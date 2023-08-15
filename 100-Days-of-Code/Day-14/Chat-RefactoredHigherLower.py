# A new approach to the "Higher or Lower" game using OOP
from game_data import data
from art import *
import random
class HigherOrLowerGame:
    def __init__(self, data):
        self.data = data
        self.score = 0
        self.current_choice = None
        self.next_choice = None

    def roll_dice(self):
        return random.choice(self.data)

    def setup_game(self):
        self.current_choice = self.roll_dice()
        self.next_choice = self.roll_dice()

        while self.next_choice == self.current_choice:
            self.next_choice = self.roll_dice()

        self.display_choices()

    def display_choices(self):
        print(f"Compare A: {self.current_choice['name']}, a {self.current_choice['description']}, from {self.current_choice['country']}")
        print(vs)
        print(f"Compare B: {self.next_choice['name']}, a {self.next_choice['description']}, from {self.next_choice['country']}")

    def get_winner(self):
        if self.current_choice['follower_count'] > self.next_choice['follower_count']:
            return 'a'
        else:
            return 'b'

    def play_round(self):
        self.setup_game()
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == self.get_winner():
            print("You win!")
            self.score += 1
            self.current_choice = self.next_choice
        else:
            print("You lose!")
            print(f"Your score is {self.score}")
            return False

        return True

    def play_game(self):
        print(logo)
        keep_playing = True
        while keep_playing:
            keep_playing = self.play_round()
            if not keep_playing:
                play_again = input("Do you want to play the higher or lower game again? type 'y' or 'n'").lower()
                if play_again == 'y':
                    self.score = 0
                    keep_playing = True
                else:
                    print("Thanks for playing!")
                    break


# The script execution would look something like this:

game_instance = HigherOrLowerGame(data)
game_instance.play_game()

# Note: This script assumes the existence of the "data" list which contains the game data.
