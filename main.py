#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welecome to Tip Calculator")
bill = input("What is the total bill amount ? ")
Tip = input("What percentage tip would you like to pay ? 10, 12, or 15 ? ")
People = input("How many people to split the bill ? ")

Share = (float(bill)*(float(Tip)/100+1))/int(People)

print(f"Every person should pay: %.2f" %round(Share,2))
