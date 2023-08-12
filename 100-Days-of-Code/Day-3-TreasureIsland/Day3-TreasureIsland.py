print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

l_or_r = input("\nWould you like to travel left of right on your journey? ")

if l_or_r.lower() == "l":
  swim_or_wait = input("\nWould you like to SWIM forward or WAIT at this lovely palm tree? SWIM or WAIT? ")
  if swim_or_wait.lower() == "wait":
    door = input("\nWhich door would you like to take to furture your quest? RED, BLUE or YELLOW? ")
    if door.lower() == "red":
      print("\nYou have been burnt to a crisp by the firelord!\n\nGAME OVER!!")
    elif door.lower() == "blue":
      print("\nYou have been eaten by dinosaur!\nGAME OVER!!")
    elif door.lower() == "yellow":
      #print("\nYou are the true master of the dungeon and have completed the quest!\nGold and Riches await you at the Tavern!\n\nGAME COMPLETED!")
      horse = input("\nDo you want to ride the horse through the forest? Y or N ")
      if horse.lower() == "y":
        pet = input("\nFor a pet would you like a pet Spider or a pet Dog? SPIDER or DOG? ")
        if pet.lower() == "spider":
          colour_pet = input("\nDo you like a Red Strawberry, Yellow Pinapple or a Blue Blueberry? RED, YELLOW, BLUE? ")
          if colour_pet.lower() == "yellow":
              print("\nYour pineapple turnes into a goblin and eats you!\n\nGAME OVER!!")
          elif colour_pet.lower() == "red":
              print("\nYour Strawberry is poisoned you die!\n\nGAME OVER!!")
          elif colour_pet.lower() == "blue":
              print("\nYou are the true master of the dungeon and have completed the quest!\nGold and Riches await you at the Tavern!\n\nGAME COMPLETED!")
          else:
            print("GAME OVER")
        else:
          print("\nYour dog pee pees on your leg, but the wee is acid and you die!\n\nGAME OVER!!")
      else:
        print("\nA crocidille jumps out of the swamp and eats you!\n\nGAME OVER!!")
    else:
      print("GAME OVER")
  else:
    print("\nYou have been eaten by a huge shark and died!\n\nGAME OVER!!")
else:
  print("\nYou have fallen in a lava pit and died!\n\nGAME OVER!!")
  
    

