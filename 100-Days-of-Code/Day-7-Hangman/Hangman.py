#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 
lives = 5

trys = []
while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already guessed that letter.")
        continue
    if guess in trys:
        print("You've already guessed that letter.")
        continue
    # Check guessed letter
    found = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            found = True
    if not found:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}\n")
        trys.append(guess)  # Use append() to add the guessed letter to the trys list
        print(f"Letters already guessed\n{trys}\n\n")
# ...

    
    print(f"{display}\n\n--------------------------------------")

if "_" not in display:
    print("Congratulations, you've guessed the word!")
else:
    print("Sorry, you're out of lives. The word was:", chosen_word)

  

