import random

list = [0, 1, 2]

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
---'    ____)____
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
game_options = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.choice(list)

print("\nYou chose:")
print(game_options[human_choice])
print("\n")
print("Computer chose:")
print(game_options[comp_choice])
print("\n")

if(human_choice == comp_choice):
    print("Draw.")
    print("\n")

elif(human_choice==0):
    if(comp_choice==1):
        print("Computer wins!")
        print("\n")
    elif(comp_choice==2):
        print("You win!")
        print("\n")

elif(human_choice==1):
    if(comp_choice==0):
        print("You win!")
        print("\n")
    elif(comp_choice==2):
        print("Computer wins!")
        print("\n")

elif(human_choice==2):
    if(comp_choice==0):
        print("Computer wins!")
        print("\n")
    elif(comp_choice==1):
        print("You win!")
        print("\n")