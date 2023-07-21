import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image = [rock, paper, scissors]
# print(image[0])

get_input = int(input("Type 0 for Rock, 1 for Paper, 2 Scissors: "))
print(f"You chose: \n {image[get_input]}")

comp_input = random.randint(0,2)
print(f"Computer chose: \n {image[comp_input]}")

if(get_input == 0):
    if(comp_input == 1):
        print("Computer wins")
    elif(comp_input == 0):
        print('Draw')
    else:
        print("You win")
elif(get_input == 1):
    if(comp_input == 2):
        print("Computer wins")
    elif(comp_input == 1):
        print('Draw')
    else:
        print("You win")
elif(get_input == 2):
    if(comp_input == 0):
        print("Computer wins")
    elif(comp_input == 2):
        print('Draw')
    else:
        print("You win")


