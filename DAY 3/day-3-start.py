print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You are eligible")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Pay $5.")
  elif age <= 18:
    bill = 7
    print("Pay $7.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Free tickets.")
  else:
    bill = 12
    print("Pay $12.")
  photo = input("Want photo  Y or N: ")
  if photo == 'Y':
    bill += 5
    print(f"Your final bill is ${bill}:")
  else:
    print(f"Your final bill is ${bill}:")
    
    
else:
  print("You are not eligible")
