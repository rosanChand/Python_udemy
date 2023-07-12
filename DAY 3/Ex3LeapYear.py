# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if (year % 4) == 0:
#     check = True
# elif(year % 100) == 0:
#     check = False
# elif(year%400) == 0:
#     check = True
# else:
#     check = False

# if(check == True):
#     print("Leap year.")
# else:
#     print("Not leap year.")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
