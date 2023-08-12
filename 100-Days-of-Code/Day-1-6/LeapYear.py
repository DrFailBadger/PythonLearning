# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 == 0:
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

## create me a simple function to find if a date is a leap yar
# def is_leap(year):
#     if year % 4 == 0:
#         print("year has no remainder and is divisable by 4")
#         # if year % 100 has remainder:
#         if year % 100 != 0:
#             print("year does not evenly divide by 100")
#         if year % 400 == 0:
#             print("year doesy divide by 400 not leap year")
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is not a leap year")
#
# is_leap(2020)
# is_leap(2021)
# is_leap(2022)
