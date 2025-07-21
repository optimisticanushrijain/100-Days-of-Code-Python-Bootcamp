print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_tip = bill * (tip/100 + 1)
# print(bill_tip)
print(round(bill_tip))
person_contribution = bill_tip/people
# print(person_contribution)
final_res=round(person_contribution, 2)
print(f"Each person should pay: {final_res}")
print("Each person should pay: " + str(final_res))




