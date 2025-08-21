import random
import string

print("Password_generator")

length = int(input("Enter lenght password: "))
include_numbers = input("With numbers (yes/no): ")
include_symbols = input("With symbols (yes/no): ")

all_chars = string.ascii_letters
if include_numbers == "yes":
    all_chars += string.digits
if include_symbols == "yes":
    all_chars +=  string.punctuation

password = " "   

for i in range(length):
    password += random.choice  (all_chars) 

print("Password: ")
print(password)

