import random
import os
treasure = random.randint(1,9) * 11

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row4 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row5 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row6 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row7 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row8 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row9 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
map = [row1, row2, row3, row4, row5, row6, row7,row8,row9]
used_positions = set()
gamewon = False
while not gamewon:
    #os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(treasure)
    
    print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆
  
    #Write your code below this row 👇
    int_part1 = int(position[0])  # Convert the first character to an integer
    int_part2 = int(position[1])  # Convert the second character to an integer
    if int_part1 < 1 or int_part1 > 9 or int_part2 < 1 or int_part2 > 9:
        print("Invalid input. Please enter two digits between 1 and 9.")
        input("Press Enter to continue...")
        continue
    if position in used_positions:
        print("This position has already been entered.")
        input("Press Enter to continue...")
        continue  
    used_positions.add(position)

    if  treasure == int(position) :
        map[int_part1 -1][int_part2 -1] = "O"
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}")
        print(f"You have found the treasure on square {position}")
        input("Press Enter to continue...")
        gamewon = True

    else:
        map[int_part1 -1][int_part2 -1] = "X"
        print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}")
        
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console55