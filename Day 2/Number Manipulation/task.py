# Coding Exercise 4: BMI Calculator
bmi = 84 / 1.65 ** 2
print(bmi) # o/p = 30.85399449035813

###Flooring a number (remove all decimal places)
print(int(bmi)) # o/p = 30

###Rounding a Number (Traditional Mathematical Sense)
# -below 0.5, above 0.5 or equal to 0.5
# round(number, number_of_digits)
#Parameter Description
#number	   Required. The number to be rounded
#digits	   Optional. The number of decimals to use when rounding the number. Default is 0
print(round(30.85399449035813))  #o/p = 31
print(round(30.4)) # o/p = 30
print(round(3.5)) # o/p = 4 , #rounds to the nearest even integer
print(round(bmi, 2)) # o/p = 30.85

######Assignment Operators (to manipulate a value based on the previous value)
score = 0
#User scores a point
score += 1
print(score)

######## f-strings (Mixing strings and different data types)
# To specify a string as an f-string, simply put an f in front of the string literal, like below:
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
# More read: https://www.w3schools.com/python/python_string_formatting.asp
print("Your score is " + str(score)) #painful process

#More convenient is to use f-strings
score = 0  #int
height = 1.8  #float
is_winning= True  #boolean
print(f"") #LIKE THIS
print(f"Your score is = + score, your height is {height}. You are winning is {is_winning}" )
# So, all of these different data types are combined into a string - LIKE THIS above

name = input("What is your name?")
print(f"Hello, {name}")
age=12
print(f"You are {age} years old")

#QUIZ 3: MATHEMATICAL OPERATIONS QUIZ
print(6 + 4 / 2 - (1 * 2))
# print(6 + 4 / 2 - 2)
# print(6 + 2.0 - 2)
# print(8.0 - 2)
# print(6.0)

a = int("5") / int(2.7)
# int("5") = 5
# int(2.7) = 2
# a = 5 / 2 = 2.5 = float
