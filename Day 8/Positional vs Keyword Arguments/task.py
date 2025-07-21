# #  Functions with input
#
# # def greet_with_name(name):
# #     print(f"Hello {name}")
# #     print(f"How do you do {name}?")
# #
# #
# # greet_with_name("Jack Bauer")
# #
# # def greet_with_name_location(name, location, address):
# #     print(f"Hello, {name}")
# #     print(f"what is your {location}?")
# #     print(f"Your addresses is : {address}")
# #
# # greet_with_name_location(location="Chicago", name="Anu", address="Illinois")
#
#
#
# #LOVE CALCULATOR
# def calculate_love_score(name1, name2):
#     #name1= string, name2=string
#     #1. Combine 2 strings- named as combined_strings - Concatenate
#     #2. convert it into lowercase using lower()
#     #Step 1:
#     combined_strings = name1 + name2
#     print(combined_strings)
#     #Step 2:
#     combined_strings_lower = combined_strings.lower()
#     print(combined_strings_lower)
#     t = combined_strings_lower.count("t")
#     r = combined_strings_lower.count("r")
#     u = combined_strings_lower.count("u")
#     e = combined_strings_lower.count("e")
#     first_dig = t + r + u + e
#     print(first_dig)
#
#     l = combined_strings_lower.count("l")
#     o = combined_strings_lower.count("o")
#     v = combined_strings_lower.count("v")
#     e = combined_strings_lower.count("e")
#     second_dig = l + o + v + e
#     print(second_dig)
#
#     score = str(first_dig) + str(second_dig)
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")

def my_function(a,b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)
my_function(b=7, d=90, a=8, c=99)