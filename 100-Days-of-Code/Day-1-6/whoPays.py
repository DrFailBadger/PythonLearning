# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenght = len(names)
print(lenght)
random_name =int(random.randint(0,lenght -1))
who_buys = names[random_name]
print(f"{who_buys} is going to buy the meal today!")
#print(name[random_name])