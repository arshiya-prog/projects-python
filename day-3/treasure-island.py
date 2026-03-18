print("Welcome to Treasure Island!\nYour goal is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
direction = input("Left or Right? ").lower()
print("\n")

if direction == "left":
    print("You've come to a lake. There is an island at the middle of the lake.")
    action = input('Type "Wait" to wait for a boat or "Swim" to swim across: ').lower()
    print("\n")

    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color_choice = input("Red, Yellow and Blue. Which do you choose? ").lower()
        print("\n")

        if color_choice == "red":
            print("Burnt by fire. Game over.")
            print("\n")
        elif color_choice == "yellow":
            print("You win!")
            print("\n")
        elif color_choice == "blue":
            print("Eaten by beasts. Game over.")
            print("\n")
        else:
            print("Game over.")
            print("\n")
    
    else:
        print("Attacked by trout. Game over.")
        print("\n")

else:
    print("Fell into a hole. Game Over.")
    print("\n")
