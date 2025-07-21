import art
import random

print(art.logo1)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")


def computer_guess():#45
    right_number = random.randint(1, 100)
    return right_number

def compare():
    attempts_easy = 10
    attempts_hard = 5
    c_guess = computer_guess()
    print(c_guess)
    is_correct_guess = False
    while not is_correct_guess:
        if choice == "hard":
            print(f"You have {attempts_hard} attempts remaining to guess the number. ")
            attempts_hard = attempts_hard - 1
        elif choice == "easy":
            print(f"You have {attempts_easy} attempts remaining to guess the number. ")
            attempts_easy = attempts_easy - 1

        user_guess = int(input("Make a guess: "))
        if user_guess == c_guess:
            is_correct_guess = True
            print(f"You got it! The answer was {c_guess}.")
        elif attempts_hard == 0 or attempts_easy == 0:
            is_correct_guess = True
            print("You've run out of guesses. Refresh the page to run again.")
        elif user_guess < c_guess:
            print("Too low.\nGuess again.")
        elif user_guess > c_guess:
            print("Too high.\nGuess again.")


compare()







