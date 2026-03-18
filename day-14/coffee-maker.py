import sys

resources = {
    "water":100,
    "milk":50,
    "coffee":76,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

balance_in_machine = 0
cont = 0

def are_resources_sufficient(order):
    for key in MENU[order]["ingredients"]:
        if resources[key] < MENU[order]["ingredients"][key]:
            return False
    return True
        
def take_money():
    penny = int(input("Insert pennies: "))
    nickle = int(input("Insert nickles: "))
    dime = int(input("Insert dimes: "))
    quarter = int(input("Insert quarters: "))

    total_money = (0.01*penny) + (0.05*nickle) + (0.10*dime) + (0.25*quarter)
    return total_money

def is_transaction_successful(order):
    money_paid = take_money()
    actual_amount = MENU[order]["cost"]

    if actual_amount > money_paid:
        return money_paid, False
    else:
         return money_paid, True

def make_coffee(order):
    for key in MENU[order]["ingredients"]:
        resources[key] -= MENU[order]["ingredients"][key]
    print(f"\nYour {order} is ready!\n")
    

while cont == 0:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        print(f"money : ${balance_in_machine}")

    elif order == "off":
        sys.exit()

    else:
        if are_resources_sufficient(order):
            money_paid_by_customer, transaction_successful = is_transaction_successful(order)
            actual_amount = MENU[order]["cost"]
            if transaction_successful == False:
                    print("Insufficient money. Money refunded!")
            else:
                if actual_amount == money_paid_by_customer:
                    balance_in_machine += money_paid_by_customer
                    make_coffee(order)
                elif actual_amount < money_paid_by_customer:
                    change = round(money_paid_by_customer - actual_amount, 2)
                    make_coffee(order)
                    print(f"Here is ${change} in change.")
                    balance_in_machine += actual_amount

        else:
            for key in MENU[order]["ingredients"]:
                if MENU[order]["ingredients"][key] > resources[key]:
                    print(f"Sorry there is not enough {key}")