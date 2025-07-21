import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidder_dict):
    winner=""
    highest_bid=0
    for ele in bidder_dict:
        bid_amount_value=bidder_dict[ele]
        if bid_amount_value > highest_bid:
            highest_bid = bid_amount_value
            winner = ele
    print(f"The winner is {winner} with a bid of ${highest_bid}")


my_data = {}
user_hits=True
while user_hits:
    user_name = input("What is your name?: ").lower()
    bid_amount = int(input("What is your bid?: $"))
    my_data[user_name] = bid_amount
    should_continue = input(("Are there any other bidders? Type 'yes or 'no'. ")).lower()
    if should_continue == "yes":
        print("\n" * 20)
    elif should_continue == "no":
        user_hits = False
        # simply can use the max() function as well, but as a beginner it's good to write the whole logic
        #res_max = max(my_data, key=my_data.get)
        find_highest_bidder(my_data)







