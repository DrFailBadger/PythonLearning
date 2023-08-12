# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
days_in_year = 365
months_in_year = 12
weeks_in_year = 52

years_left = 90 - age_as_int
days_left = years_left * days_in_year
months_left = years_left * months_in_year
weeks_left = years_left * weeks_in_year

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left in your life.")




