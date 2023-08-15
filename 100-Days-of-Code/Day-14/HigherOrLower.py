from game_data import data
from art import *
import random

def roll_dice():
    dice =random.choice(data)
    return dice

def set_gameup():
    compare_a = roll_dice()
    text_a = (f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    compare_b = roll_dice()
    text_b = (f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    print (text_a)
    print(f"A Follower Count:{compare_a['follower_count']} vs B Follower Count:{compare_b['follower_count']}")
    print (vs)
    print (text_b)
    choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
    return compare_a, compare_b, choice

def compare_data(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'

def player_win(choice_of_player, compare_func):
    actual_winner = compare_func(choice_of_player[0], choice_of_player[1])
    if choice_of_player[2] == actual_winner:
        return True
    else:
        return False
    
def game(compare_func, win_func, score):
    choice_of_player = set_gameup()
    if win_func(choice_of_player, compare_func):
        print("You win")
        score += 1
        return score, True
    else:
        print("You lose")
        print(f"Your score is {score}")
        return score, False

def main(compare_func, win_func):
    score = 0
    keep_playing = True
    
    while keep_playing:
        # Uncomment the next line if you have a logo to display
        print(logo)
        
        score, keep_playing = game(compare_func, win_func, score)
        if not keep_playing:
            play_again = str(input("Do you want to play the higher or lower game again? type 'y' or 'n'")).lower()
            if play_again == 'y':
                score = 0
                keep_playing = True
            else:
                print("Thanks for playing!")
                break

      
if __name__ == "__main__":
  main(compare_data, player_win)