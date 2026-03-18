import random

print("Welcome to the PyPassword Generator!")

letters = []
symbols = []
numbers = []
pw = []

for i in range(65, 91):
    letters.append(chr(i))
for i in range(97, 123):
    letters.append(chr(i))
for i in range(0, 10):
    numbers.append(str(i))
for i in range(33, 39):
    symbols.append(chr(i))

no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))

for i in range(0, no_of_letters):
    l = random.choice(letters)
    pw.append(l)
for i in range(0, no_of_symbols):
    s = random.choice(symbols)
    pw.append(s)
for i in range(0, no_of_numbers):
    n = random.choice(numbers)
    pw.append(n)

password = random.sample(pw, len(pw))
password = "".join(password)
print(f"Your password is: {password}")