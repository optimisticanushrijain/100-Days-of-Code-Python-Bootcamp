import random
import art
from game_data import data



# def random_data_generate_A():
#     random_indexA = random.randrange(len(data))
#     str1 = data[random_indexA]["name"]
#     str2 = data[random_indexA]["description"]
#     str3 = data[random_indexA]["country"]
#     str4 = data[random_indexA]["follower_count"]
#     print("Compare A: " + str1 + ", " + "a " + str2 + ", " + "from " + str3 + ".")
#
# def random_data_generate_B():
#     random_indexB = random.randrange(len(data))
#     str1 = data[random_indexB]["name"]
#     str2 = data[random_indexB]["description"]
#     str3 = data[random_indexB]["country"]
#     print("Against B: " + str1 + ", " + "a " + str2 + ", " + "from " + str3 + ".")

# TO DO: I - Import logo
print(art.logo)
current_score = 0
should_continue = True
##random_data_generate_A()
while should_continue:
    # TO DO: II - Generate random data from the list of dictionary:
    # 1. Which function does this? random module > randrange
    random_indexA = random.randrange(len(data))
    # 2. how to print a single dictionary randomly? some values from that dictionary
    A1 = data[random_indexA]["name"]
    A2 = data[random_indexA]["description"]
    A3 = data[random_indexA]["country"]
    A4 = data[random_indexA]["follower_count"]

    # 3. printing
    print("Compare A: " + A1 + ", " + "a " + A2 + ", " + "from " + A3 + ".")
    # TO DO: I - Import logo
    print(art.vs)
    #random_data_generate_B()
    random_indexB = random.randrange(len(data))
    B1 = data[random_indexB]["name"]
    B2 = data[random_indexB]["description"]
    B3 = data[random_indexB]["country"]
    B4 = data[random_indexB]["follower_count"]
    print("Against B: " + B1 + ", " + "a " + B2 + ", " + "from " + B3 + ".")
    user_input = input("Who has more followers? Type 'A' or 'B': ")

    def compare_answers():
        if  A4 > B4:
              current_score += 1
              print(f"You're right! Current score: {current_score}.")
              # # Swapping
              # A1 = B1
              # A2 = B2
              # A3 = B3
              # A1 = data[random_indexA]["name"]
              # A2 = data[random_indexA]["description"]
              # A3 = data[random_indexA]["country"]
              # # calling function()

        else:
            print(f"Sorry, that's wrong. Final score: {current_score}") # Game Over
            should_continue = False

    if user_input =="A":
        compare_answers()
    elif user_input == "B":
        compare_answers()





