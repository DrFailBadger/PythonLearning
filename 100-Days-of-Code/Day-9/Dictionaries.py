programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "loop": "The action of doing something over and over again.",
}

# add to a dictionary
programming_dictionary["loooper"] = "adasdsadsadad"

#print(programming_dictionary)
empty_dic = {}

#wipe existing
#programming_dictionary = {}
#print(programming_dictionary)

#changing a value in a dict
programming_dictionary["Bug"] = "A new entry"
#print(programming_dictionary)

# loop thoough dic
for key in programming_dictionary:
  print(key) # prints keys
  print(programming_dictionary[key]) # prints values
