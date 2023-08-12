#Step 4

import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
exclude = ["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",";",":","'","<",">",",",".","/","?","`","~"]
end_of_game = False
#word_list = ["ardvark", "baboon", "camel"]
#chosen_word = random.choice(word_list)
chosen_word = None
# while chosen_word not None:
#     chosen_word = input("Please provide word? ")
while chosen_word == None:
    chosen_word = input("Please provide word? ").lower()
    for char in chosen_word:
        if char in exclude:
            print("Please enter only letters.")
            chosen_word = None
            break
#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
# create list of numbers and special characters to be excluded from guess

#Create blanks
lives = 6
trys = []
display = []
for _ in range(word_length):
    if chosen_word[_] == " ":
        display += " "
    else:
        display += "_"
#'print (chosen_word)
while not end_of_game and lives > 0:
    #sleep 5 seconds
    # only clear screen after before guess
    #os.system('cls' if os.name == 'nt' else 'clear')
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        print("Please enter only one letter.")
        print(f"{' '.join(display)}")
        continue
    if guess in exclude:
        print("Please enter only letters not numbers or special characters.")
        print(f"{' '.join(display)}")
        continue
    if guess in display:
        print("You've already guessed that letter.")
        print(f"{' '.join(display)}")
        continue
    if guess in trys:
        print("You've already guessed that letter.")
        print(f"{' '.join(display)}")
        continue
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print("you guessed correctly!\n")
            #print(f"{' '.join(display)}")


            #print(stages[lives])

    #TODO-2: - If guess is not a letter in the chosen_word,
    if guess not in chosen_word:
        lives -= 1
        trys += guess
        print(f"Guesed Letters:\n{trys}\n")
        print(f"You guessed wrong!\n You have {lives} lives left!")
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.\n")
    elif lives == 0:
        end_of_game = True
        print(stages[lives])
        print(f"You loose.\nThe word was:{chosen_word}\n")
        
      
