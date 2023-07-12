#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("*****TIP Calulator*****")
bill = input("what was the total bill? : ")
t_bill = float(bill)
tip = input("What % ti would you like to give? 10%, 12%, 15%? ")
t_tip = int(tip)
peo = input("How many people to split the bill: ")
t_peo = int(peo)
t_bill += (t_bill*(t_tip/100))
total = round(t_bill/t_peo, 2)
total = "{:.2f}".format(total)
print("Every person should pay: ",total)