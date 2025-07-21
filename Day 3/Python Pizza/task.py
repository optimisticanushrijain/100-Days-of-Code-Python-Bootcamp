print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "s":
    bill = 15
    # print("For Small size you have to pay the bill: $15")
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    # print("For Medium size you have to pay the bill: $20")
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
else:
    print("You entered the wrong choice: ")
    # print("For Large size you have to pay the bill: $25")
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

