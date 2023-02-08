from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_Machine = CoffeeMaker()
menu = Menu()
register = MoneyMachine()
is_on = True
while is_on:
    order = input(f'What would you like? ({menu.get_items()}): ')  # prompts user for what item
    if order == "report":
        coffee_Machine.report()
        register.report()
    elif order == "latte" or order == "espresso" or order == "cappuccino":
        item = menu.find_drink(order)  # checks to make sure the item is on the menu
        can_Make = coffee_Machine.is_resource_sufficient(item)
        if can_Make:
            can_Pay = register.make_payment(item.cost)
            if can_Pay:
                coffee_Machine.make_coffee(item)
    elif order == "off":
        print("Good bye")
        is_on = False


#print(order)
