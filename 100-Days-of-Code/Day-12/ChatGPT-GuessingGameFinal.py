# Streamlined version of the guessing game

from art import logo
import random

def choose_difficulty():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Invalid choice. Please select 'easy' or 'hard'.")

def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please choose a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def game():
    attempts = choose_difficulty()
    number = random.randint(1, 100)
    print(f"Psst, the correct answer is {number}")

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = get_guess()

        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            return

        attempts -= 1

    print("You've run out of guesses, you lose.")

def main():
    while True:
        print(logo)
        game()
        play_again = input("Do you want to play another game of the guessing game? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


