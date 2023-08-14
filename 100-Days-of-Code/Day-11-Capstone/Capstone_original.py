############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
logo = '''

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/          


'''
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## 
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True
while play_again:
  print(logo )
  players_dic = {
    "player" : [],
    "dealer" : [],
    
  }
  PLAYER = players_dic["player"]
  DEALER = players_dic["dealer"]
  
  
  def deal_card(name):
    '''Deals a card to 'name' '''
    card = random.choice(cards)
    name.append(card)
  

  def  players_score(p1):
    p1_total = sum(p1)
    #print(p1_total)
    player_continues = True
    while player_continues:
        if p1_total < 21:
          newcard = str(input(f"Would you like to draw a new card? Type 'y' for new card or 'n' to stick: ")).lower()
          if newcard == "y":
                deal_card(p1)
                p1_total = sum(p1)
                player1_score = p1_total
                print(f"{list(players_dic.keys())[0]} cards:{p1} total: {p1_total}")
                if p1_total > 21:
                  player_continues = False
          elif newcard == "n":
                player_continues = False
        else: 
          player_continues = False
    return p1_total

  def computer_score(p2, p1):
    below = True
    p2_total = sum(p2)
    while below:
      deal_card(p2)
      p2_total = sum(p2)
      print(f"{list(players_dic.keys())[1]} is below 17 drawing card, cards{p2} total: {p2_total}")
      if p2_total > 21:
        return print(f"{list(players_dic.keys())[1]} is bust, {list(players_dic.keys())[0]} WINS!")
        below = False
      elif p2_total > p1:
        below = False
    return p2_total


    
  def who_wins(p1,p2):
    py1 = players_score(p1)
    py2 = sum(p2)
    if py1 > 21:
      result = f"{list(players_dic.keys())[0]} is bust, {list(players_dic.keys())[1]} WINS!"
      return result
    elif py2 <= py1 and py2 <17:
      computer_score(p2,py1)
    elif py2 > 21:
      result = f"{list(players_dic.keys())[1]} is bust, {list(players_dic.keys())[0]} WINS!"
      return result
    elif py1 == 21 and py2 == 21:
      result = "Draw"
      return  result
    elif py1== 21:
      result = f"{list(players_dic.keys())[0]} is the Winner with: BLACKJACK! {py1}"
      return result
    elif py2 == 21:
      result = f"{list(players_dic.keys())[1]} is the Winner with: BLACKJACK! {py2}"
      return result
    elif py1 > py2 :
      result = f"{list(players_dic.keys())[0]} is the Winner with: {py1} | {list(players_dic.keys())[1]} has: {py2} "
      return result
    elif py2 > py1 :
      result = f"{list(players_dic.keys())[1]} is the Winner with: {py2}| {list(players_dic.keys())[0]} has: {py1} "
      return result
    elif py2 == py1:
      result = "Draw"
      return  result

  #Starting hands
  deal_card(PLAYER)
  deal_card(PLAYER)
  if sum(PLAYER) == 21:
    print(f"Your cards: {PLAYER}: BLACKJACK!!")
  else:
    print(f"Your cards: {PLAYER} ")  
  
  deal_card(DEALER)
  print(f"Dealers first card: {DEALER} ")
  deal_card(DEALER)
  #print(f"Dealers card: {DEALER} ")
  print(who_wins(PLAYER, DEALER))

  new_blackjack_game = str(input("Would you like to play another game of BlackJack type 'y' or 'n'")).lower()
  if new_blackjack_game == "n":
    play_again = False