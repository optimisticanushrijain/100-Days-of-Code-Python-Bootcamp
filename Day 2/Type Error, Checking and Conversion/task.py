# PAUSE 1:
# FIXING this TypeError- len(12345)
print(len("12345")) # o/p = 5

# PAUSE 2:
# TYPE CHECKING - using function type(<a piece of data of any data type>)
print(type("AnushriJ")) # o/p = <class 'str'>
print(type('Hey')) # o/p = <class 'str'>
print(type(123456)) # o/p = <class 'int'>
print(type(123_456)) # o/p = <class 'int'>
print(type(3.1457)) # o/p = <class 'float'>
print(type(True)) # o/p = <class 'bool'>

# TYPE CONVERSION or TYPE CASTING
print("123" + "456") # o/p = 123456

# I want to add these numbers
print(int("123") + int("456")) # o/p = 579, int type casting

# Can't convert abc into number
# Gives this error - ValueError: invalid literal for int() with base 10: 'abc'
# print(int("abc") + int("456"))

print(bool("true")) #Boolean type casting

#USING FOLLOWING FUNCTIONS
float()
int()
str()
bool()

#PAUSE 3.
# Make this line of code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))

## SOLUTION STEPS:
user_name = input("Enter your name")
length_name = len(user_name)

## Checking type of these
print(type("Number of letters in your name: ")) #str
print(type(length_name)) #int

#FIX: TYPE CASTING / TYPE CONVERSION using str() function
print("Number of letters in your name: " + str(length_name))
# o/p = 7 if i/p = anushri




