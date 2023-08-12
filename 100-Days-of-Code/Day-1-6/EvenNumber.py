#Write your code below this row 👇
odd = 0
for number in range(1,101):
  if number % 2 == 0:
    print(number)
    odd += number
print(odd)

odd1 = 0
for number in range(2,101,2):
  print(number)
  odd1 += number
print(odd1)
