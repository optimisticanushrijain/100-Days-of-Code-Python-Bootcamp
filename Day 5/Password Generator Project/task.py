import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy level
# password = ""
#
# # nr_letters = 4
# for char in range(0, 4):
#     # 1-5 # print 1-4
#    password += random.choice(letters)
# print(password)
# for char in range(0, 4):
#     # 1-5 # print 1-4
#    password += random.choice(numbers)
# print(password)
# for char in range(0, 4):
#     # 1-5 # print 1-4
#    password += random.choice(symbols)
# print(password)

# Hard level
# password =""
# # x$d24g*f9 -> 4, 3, 2
# for char in range(0, nr_letters +1):
#     # 1-5 # print 1-4
#    password += random.choice(letters)
#
# for char in range(0, nr_numbers + 1):
#     # 1-5 # print 1-4
#    password += random.choice(numbers)
#
# for char in range(0, nr_symbols + 1):
#     # 1-5 # print 1-4
#    password += random.choice(symbols)
#
# print(password)
# my_list = list(password)
# random.shuffle(my_list)
# my_string = "".join(my_list)
# print(my_string)

# Hard level - Another way
password_list = []
password = ""
# x$d24g*f9 -> 4, 3, 2
for char in range(0, nr_letters):
   # password_list += random.choice(letters)
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
   password_list += random.choice(numbers)

for char in range(0, nr_symbols):
   password_list += random.choice(symbols)
print(password_list)
print(random.shuffle(password_list))
print(password_list)

#back to string
for char in password_list:
    password += char
print(f"Your password is: {password}")
