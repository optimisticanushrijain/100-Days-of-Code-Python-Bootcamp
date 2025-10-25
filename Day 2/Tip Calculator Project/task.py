print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
bill_tip = bill * (tip_as_percent + 1)
# print(bill_tip)
bill_per_person = bill_tip/people
# print(bill_per_person)
final_amount=round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")
print("Each person should pay: " + str(final_amount))
print(f"Each person should pay: ${round(bill_per_person, 2)}")

# print(round(150 * 1.12 / 5, 2))
# print(round(150 / 5 * 1.12, 2))
# print(12/100)
# print(150 * (1 + 12/100))
# print((150/5) * (1+12/100))




