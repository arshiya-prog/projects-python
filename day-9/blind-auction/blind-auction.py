import os
import logo

print(logo.logo)

auction = {"name":[], "bid":[]}

def blind_auction():
    max_bid = 0
    winner_name = ""
    n = input("What is your name? ")
    b = int(input("What is your bid? $"))

    auction["name"].append(n)
    auction["bid"].append(b)

    max_bid = max(auction["bid"]) # checks all bids and selects the maximum one
    winner_index = auction["bid"].index(max_bid)
    winner_name = auction["name"][winner_index]
    
    return winner_name, max_bid

cont = 0

while (cont == 0):
    winner, bid = blind_auction()

    user_input = input("Are there any other bidders? Type 'y' or 'n': ")

    if user_input == 'y':
        os.system('clear')
        continue
    elif user_input == 'n':
        print(f"The winner is {winner} with a bid of ${bid}")
        cont = 1
    else:
        print("Invalid input")