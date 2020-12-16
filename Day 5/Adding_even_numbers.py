#Write your code below this row 👇
#adding even numbers 

total = 0
for num in range(1,101):
  if num % 2 == 0:
    total += num
print(total)

totals = 0
for number in range(2,101,2):
  totals += number
print(totals)
