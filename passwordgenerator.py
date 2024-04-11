#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

pwd = ""
for i in range(0,nr_letters+1):
  pwd += random.choice(letters)
for i in range(0,nr_symbols+1):
  pwd += random.choice(symbols)
for i in range(0,nr_numbers+1):
  pwd += random.choice(numbers)
print(f"Ordered password generated = {pwd}\n")
  
#Hard Level - Order of characters randomised:

pwd = [] #created a pwd list for randomizing the order
for i in range(0,nr_letters+1):
  pwd += random.choice(letters)
for i in range(0,nr_symbols+1):
  pwd += random.choice(symbols)
for i in range(0,nr_numbers+1):
  pwd += random.choice(numbers)
random.shuffle(pwd) #shuffle is used to randomize the elements of the list
pwd = "".join(pwd) #convert list to string
print(f"Randomized(strong) password generated = {pwd}\n")
