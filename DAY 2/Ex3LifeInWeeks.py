# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left_alive = 90 - int(age)
day = left_alive * 365
week = left_alive * 52
month = left_alive * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")
