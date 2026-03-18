from art import logo, vs
from game_data import data
import random

print(logo)
game_still_on = 0
score = 0
choice1 = random.choice(data)

while(game_still_on == 0):
    choice2 = random.choice(data)

    if choice1 == choice2:
        choice2 = random.choice(data)

    name1 = choice1["name"]
    follower_count1 = choice1["follower_count"]
    description1 = choice1["description"]
    country1 = choice1["country"]

    name2 = choice2["name"]
    follower_count2 = choice2["follower_count"]
    description2 = choice2["description"]
    country2 = choice2["country"]

    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Compare B: {name2}, a {description2}, from {country2}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == 'a' and follower_count1 > follower_count2:
        score += 1
        print(f"\nYou're right! Current score: {score}\n")
        choice1 = choice2
    elif user_input == 'b' and follower_count1 < follower_count2:
        score += 1
        print(f"\nYou're right! Current score: {score}\n")
        choice1 = choice2
    else:
        print(f"\nSorry, that's wrong! Final score: {score}\n")
        game_still_on = 1