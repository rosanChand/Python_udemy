
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# total_size = nr_letters + nr_symbols + nr_numbers 


keyletters  =[]
keysymbols = []
keynumbers = []
for i in range(0,nr_letters):
    forletter = random.randint(0, len(letters)-1)
    keyletters.append(letters[forletter])
    
for j in range(0,nr_symbols):
    forsym = random.randint(0,len(symbols)-1)
    keysymbols.append(numbers[forsym])

for i in range(0,nr_numbers):
    fornum = random.randint(0, len(numbers)-1)
    keynumbers.append(numbers[fornum])

# print(keyletters)
# print(keysymbols)
# print(keynumbers)

#print("Here is ypur password: " + passw)
easykey = keyletters + keysymbols + keynumbers
print("Here is Your Password in order of letters, Symbols and numbers respectively: ")
print(*easykey,sep='')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("Here is Your Password in Random Order: ")
for i in range(0,len(easykey)):
    anyvalue = random.randint(0,len(easykey)-1)
   
    print(*easykey[anyvalue],end='')
print()

