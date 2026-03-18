from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

money = 0

while True:
    opt = menu.get_items()
    # print(opt)
    order = input(f"What would you like? ({opt}): ").lower()

    if order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        
        if coffee_maker.is_resource_sufficient(drink):
            for item in menu.menu:
                if item.name == order:
                    money = item.cost
            if money_machine.make_payment(money):
                coffee_maker.make_coffee(drink)