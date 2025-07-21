import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choose_list = [rock, paper, scissors]

you_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or "
                   "2 for Scissors\n"))
# if you_choose == 0: #you choose_logic
#     print(rock)
# elif you_choose == 1:
#     print(paper)
# elif you_choose == 2:
#     print(scissors)
# else:
#     print("nothing to print, wrong choice")

if you_choose >= 0 and you_choose <= 2:
    print(computer_choose_list[you_choose])
print("Computer chose:")
#print(computer_choose_list[0])
#print(random.choice(computer_choose_list))
computer_choice = random.randint(0,2)
print(computer_choose_list[computer_choice])

#Who win, lose or draw - Rules of the Game
if you_choose == 0:
    if computer_choice == 2 :
        print("You win")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 0:
        print("You draw")
    else:
        print("Invalid choice")
elif you_choose == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 2:
        print("You lose")
    elif computer_choice == 1:
        print("You draw")
    else:
        print("Invalid choice")
elif you_choose == 2:
    if computer_choice == 1:
        print("You win")
    elif computer_choice == 0:
        print("You lose")
    elif computer_choice == 2:
        print("You draw")
    else:
        print("Invalid choice")
else:
    print("Sorry, Wrong choice, won't print anything!!!!!!")