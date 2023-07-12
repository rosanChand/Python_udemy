# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tru_total = 0
love_total = 0
lower_name1 = name1.lower()
lower_name2 = name2.lower()
length1 = len(name1)
length2 = len(name2)
for i in range(length1):
    if lower_name1[i] == 't' or lower_name1[i] == 'r' or lower_name1[i] == 'u' or lower_name1[i] == 'e':
        tru_total = tru_total + 1
    if lower_name1[i] == 'l' or lower_name1[i] == 'o' or lower_name1[i] == 'v' or lower_name1[i] == 'e':
        love_total += 1
for i in range(length2):
    if lower_name2[i] == 't' or lower_name2[i] == 'r' or lower_name2[i] == 'u' or lower_name2[i] == 'e':
        tru_total += 1
    if lower_name2[i] == 'l' or lower_name2[i] == 'o' or lower_name2[i] == 'v' or lower_name2[i] == 'e':
        love_total += 1
total = tru_total * 10 + love_total
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")


