# I'll modify the code to handle the case where the user enters an invalid number.
#https://pythontutor.com/render.html#mode=edit

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
        valid_input = False
        while not valid_input:
            try:
                guess = int(input("Make a guess: "))
                if 1 <= guess <= 100:
                    valid_input = True
                else:
                    print("Please choose a number between 1 and 100.")
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
        else:
            print("Please choose a valid number.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")

def main():
    play_again = True
    while play_again:
        print(logo)
        game()

        new_game = input(str("Do you want to play another game of the guessing game? ")).lower()
        if new_game == "no":
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()