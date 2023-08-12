import random, os
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper ,scissors]
computer_score = 0
player_score = 0

# while score is less than or equal to 3 for both players
while computer_score < 3 and player_score < 3:
  
    computer_number = random.randint(0,2)
    computers_choice = rps[computer_number]
    #print(computer_number)
    #print(computers_choice)
    #Write your code below this line 👇
    
    players_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

    if players_input < 0 or players_input > 2:
            print("Invalid input. Please enter two digits between 1 and 2.")
            input("Press Enter to continue...")
            continue
    players_choice = rps[players_input]
    #print(players_input)
    print(f"Player Chose:\n\n{players_choice}")
    print(f"Computer Chose:\n\n{computers_choice}")
    if players_input == 0 and computer_number == 1:
        print("Round Loose: Computer Wins : Rock looses vs Paper")
        computer_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 0 and computer_number == 2:
        print("Round Win: Player Wins : Rock Wins vs Scissors")
        player_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 0 and computer_number == 0:
        print("Round Draw: Rock vs Rock")
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 1 and computer_number == 0:
        print("Round Win: Player Wins : Paper Wins vs Rock")
        player_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 1 and computer_number == 1:
        print("Round Draw: Paper vs Paper")
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 1 and computer_number == 2:
        print("Round Loose: Computer Wins :  Paper looses vs Scissors")
        computer_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 2 and computer_number == 0:
        print("Round Loose: Computer Wins :  Scissors looses vs Rock")
        computer_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 2 and computer_number == 1:
        print("Round Win: Player Wins : Scissors Wins vs Paper")
        player_score += 1
        print(f"player_score: {player_score} computer_score: {computer_score}")
    elif players_input == 2 and computer_number == 2:
        print("Round Draw: Rock Scissors vs Scissors")
        print(f"player_score: {player_score} computer_score: {computer_score}")
  #os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console551

if computer_score > player_score:
    print(f"Computer Wins {computer_score} to {player_score}")
elif computer_score < player_score:
    print(f"Player Wins {player_score} to {computer_score}")
