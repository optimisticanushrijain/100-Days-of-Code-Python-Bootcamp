print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child price is $5.")
    elif age <= 18:
        bill = 7
        print("Teenage price is $7.")
    else:
        bill = 12
        print("Adult price is $12.")
    want_photos = input("if you want photos, then enter y for yes or n for No.: ")
    if want_photos == "y":
        bill += 3

    print(f"The bill you have to pay: {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
