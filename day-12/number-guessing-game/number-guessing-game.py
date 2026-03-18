from logo import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1-100...\n")

difficulty = input("Choose the difficulty level. 'easy' or 'hard': ")

if difficulty == "easy":
    guesses = 10
    print(f"You have {guesses} attempts remaining to guess the number\n")
elif difficulty == "hard":
    guesses = 5
    print(f"You have {guesses} attempts remaining to guess the number\n")

number = random.randint(1, 100)

while guesses != 0:
    user_guess = int(input("\nMake a guess: "))

    if user_guess > number:
        guesses -= 1
        print("Too high!")
        print("Guess again")
        print(f"You have {guesses} attempts remaining to guess the number\n")
    elif user_guess < number:
        guesses -= 1
        print("Too low!")
        print("Guess again")
        print(f"You have {guesses} attempts remaining to guess the number\n")
    else:
        print(f"\nYou got it! The answer was {number}.\n")
        break