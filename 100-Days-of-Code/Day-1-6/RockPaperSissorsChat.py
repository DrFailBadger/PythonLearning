import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# List of possible outcomes
outcomes = ["Draw", "Player Wins", "Computer Wins"]

# Initialize scores
computer_score = 0
player_score = 0

# Function to get choice based on index
def get_choice(number):
    return choices[number]

# Main game loop
while computer_score < 3 and player_score < 3:
    # Generate random choice for computer
    computer_number = random.randint(0, 2)
    computers_choice = get_choice(computer_number)

    # Get player's choice
    players_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    
    # Validate player's input
    if players_input < 0 or players_input > 2:
        print("Invalid input. Please enter a number between 0 and 2.")
        continue

    players_choice = get_choice(players_input)
    
    print(f"Player Chose:\n{players_choice}")
    print(f"Computer Chose:\n{computers_choice}")

    # Calculate the result of the round using modulo arithmetic
    result = (players_input - computer_number) % 3
    print(f"Round Result: {outcomes[result]}")

    # Update scores based on the result
    if result == 1:
        player_score += 1
    elif result == 2:
        computer_score += 1

    print(f"Player Score: {player_score} - Computer Score: {computer_score}")
    
print("Game Over!")

# Determine the winner based on final scores
if computer_score > player_score:
    print(f"Computer Wins {computer_score} to {player_score}")
elif computer_score < player_score:
    print(f"Player Wins {player_score} to {computer_score}")
else:
    print("It's a Draw!")
#python ##### block comment
# 

# In a traditional Rock-Paper-Scissors game, there are three possible choices: "rock", "paper", and "scissors". Each choice can be represented by a number: 0 for "rock", 1 for "paper", and 2 for "scissors".

# When the player and the computer make their choices, we can calculate the difference between the player's choice and the computer's choice. For example, if the player chooses "rock" (0) and the computer chooses "scissors" (2), the difference would be -2. However, we want the result to be in the range of -1 to 1 to easily determine the winner.

# This is where modulo arithmetic comes in. Taking the difference modulo 3 ensures that the result wraps around within the range of -1 to 1. Here's how it works:

# If the player chooses "rock" (0) and the computer chooses "scissors" (2), the difference is -2. Taking -2 % 3 gives us 1, which means the player wins ("rock" beats "scissors").

# If the player chooses "scissors" (2) and the computer chooses "paper" (1), the difference is 1. Taking 1 % 3 gives us 1, indicating the player's victory ("scissors" beats "paper").

# If the player chooses "paper" (1) and the computer chooses "rock" (0), the difference is 1. Taking 1 % 3 again gives us 1, leading to the player's win ("paper" beats "rock").

# Draw:

# Player chooses "rock" (0).
# Computer chooses "rock" (0).
# Difference is 0.
# Result: 0 % 3 = 0 (Draw).
# Player Wins:

# Player chooses "scissors" (2).
# Computer chooses "paper" (1).
# Difference is 1.
# Result: 1 % 3 = 1 (Player wins).
# Computer Wins:

# Player chooses "paper" (1).
# Computer chooses "scissors" (2).
# Difference is -1.
# Result: (-1) % 3 = 2 (Computer wins).
# So, in summary:

# Result 0 = Draw
# Result 1 = Player Wins
# Result 2 = Computer Wins

# This technique allows us to map the possible differences between player and computer choices to the three possible outcomes: draw, player wins, and computer wins, which are stored in the outcomes list. The index of the outcomes list corresponds to the result obtained from the modulo arithmetic.