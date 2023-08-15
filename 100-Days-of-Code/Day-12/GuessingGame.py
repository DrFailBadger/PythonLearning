
from art import logo
import random

def difficult():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Please choose a valid difficulty.")
    return attempts

def guess_number():
    return random.randint(1,100)

def game():
    attempts = difficult()
    number = guess_number()
    print(f"Psst, the correct answer is {number}")
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # stop users entering special chars or letters by accident
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a number.")
        if guess > number:
            print("Too high.")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            attempts -= 1
        elif guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > 100 or guess < 1:
            print("Please choose a number between 1 and 100.")
        elif guess != number:
            print("Please choose a valid number.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")


def main():
    play_again = True
    while play_again:
        print(logo)
        game()
        #play game function

        new_game = input(str("Do you want to play another game of the guessing game? ")).lower()
        if new_game == "no":
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()