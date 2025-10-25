# Addition Operator
# Use Case: Concatenation of Strings and as a Mathematical Operator
print("My age: " + str(12)) # o/p = My age: 12
print(6 + 3) # o/p = 9

#Subraction Operator
print (9 - 6) # o/p = 3

#Division Operator
print(9 / 3) # o/p = 3.0
print(type(9/3)) # <class 'float'>
print(5/3) # o/p = 1.6666666666666667
#It's something called implicit typecasting
#becuase python is implicitly converting the result here into a floating point number

#Floor Division Operator
print(9 // 3) # o/p = 3
print(type(9//3)) # <class 'int'>
print(5//3) # o/p = 1

#Multiplication Operator
print(2 * 3) # o/p = 6

#Exponentiation Operator (^)
print(2 ** 3) # o/p = 8
print(type(2 ** 3)) # <class 'int'>

#Modulo Operator/Remainder Operator
print(9%3) # o/p = 0

# PEMDASLR or BODMASLR
# ()
# **
# * OR /  # depends which is more on LHS - get more priority first
# + OR -  # depends which is more on LHS - get more priority first


# PAUSE 1.
print(3 * 3 + 3 / 3 - 3) # o/p = 7.0
# PAUSE 2.
print(3 * (3 + 3) / 3 - 3) # o/p = 3.0 # isolating it into parenthesis