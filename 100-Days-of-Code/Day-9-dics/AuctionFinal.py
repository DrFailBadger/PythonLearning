#from replit import clear
from art import logo
from art import winner
from collections import OrderedDict
#HINT: You can call clear() to clear the output in the console.


new_bidders = True
bidds = {}
while new_bidders:
  print(logo)
  name = str(input("Please provide your Name? ")).lower()
  bidd = int(input("Please provide your Bidd? "))
  def add_bids(name, bidd):
    bidds[name] = bidd
  add_bids(name, bidd)
  #clear()  
  new_players = input(str("Is there anyone else who would like to bid? Yes or No\n")).lower()
  if new_players == "no":
    new_bidders = False
    # get the max value from the dict and the key
    max_key = max(bidds, key=bidds.get)
    #clear()
    print(winner)
    print(f"Person: {max_key} won with a maximum bid of {bidds[max_key]}")
    sorted_d =OrderedDict(sorted(bidds.items(),key=lambda x: x[1], reverse = True))
    for key, value in sorted_d.items():
      print(f"{key} : {value}")