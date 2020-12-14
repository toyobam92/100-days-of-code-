print("Welcome to the tip calculator")
#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = float(input(("What is the total bill ? ")))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_percent = int(input(("What perentage tip will you like to give ? ")))
#Format the result to 2 decimal places = 33.60
num_people= int(input(("How many people are spliting the bill ? ")))

bill_per_person = bill/num_people

tip = (tip_percent/100) * bill_per_person

your_bill = round(bill_per_person + tip,2)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
your_bill= "{:.2f}".format(your_bill)
print(f"Each person should pay ${your_bill}")
