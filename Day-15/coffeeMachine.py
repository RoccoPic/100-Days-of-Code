import menu

def moneyInput():
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total = (menu.coins["quarter"] * quarter) + (menu.coins["dime"] * dime) + (menu.coins["nickel"] * nickel) + (menu.coins["penny"] * penny)
    print(f"${total}")
    return total

def changeCalc(total,coffeeAsk):
    print(total,menu.hot_Coffee[coffeeAsk]["price"])
    if total < menu.hot_Coffee[coffeeAsk]["price"]:
        print("Sorry that's not enoguh money. Money refunded.")
    elif total > menu.hot_Coffee[coffeeAsk]["price"]:
        change = total - menu.hot_Coffee[coffeeAsk]["price"]
        print(f'Here is ${change} in change.')
        print(f'Here is your {coffeeAsk}. Enjoy!')
        menu.resources["money"] = menu.resources["money"] + menu.hot_Coffee[coffeeAsk]["price"]
    elif total == menu.hot_Coffee[coffeeAsk]["price"]:
        print('No change needed.')
        print(f'Here is your {coffeeAsk}. Enjoy!')
        menu.resources["money"] = menu.resources["money"] + menu.hot_Coffee[coffeeAsk]["money"]

def makeCoffee(coffeeAsk):
    if (menu.resources["water"] >= menu.hot_Coffee[coffeeAsk]["water"]) and (menu.resources["milk"] >= menu.hot_Coffee[coffeeAsk]["milk"]) and (menu.resources["coffee"] >= menu.hot_Coffee[coffeeAsk]["coffee"]): 
        changeCalc(total,coffeeAsk)
    if menu.resources["water"] >= menu.hot_Coffee[coffeeAsk]["water"]:
        menu.resources["water"] = menu.resources["water"] - menu.hot_Coffee[coffeeAsk]["water"]
    elif menu.resources["water"] < menu.hot_Coffee[coffeeAsk]["water"]:
        print("Sorry there is not enough water.")
    if menu.resources["milk"] >= menu.hot_Coffee[coffeeAsk]["milk"]:
        menu.resources["milk"] = menu.resources["milk"] - menu.hot_Coffee[coffeeAsk]["milk"]
    elif menu.resources["milk"] < menu.hot_Coffee[coffeeAsk]["milk"]:
        print("Sorry there is not enough milk.")
    if menu.resources["coffee"] >= menu.hot_Coffee[coffeeAsk]["coffee"]:
        menu.resources["coffee"] = menu.resources["coffee"] - menu.hot_Coffee[coffeeAsk]["coffee"]
    elif menu.resources["coffee"] < menu.hot_Coffee[coffeeAsk]["coffee"]:
        print("Sorry there is not enough coffee.")

    


def coffeeMaker():
    on = True
    global total
    while(on == True):
        coffeeAsk = input("What would you like (espresso/latte/cappuccino): ")
        if coffeeAsk == "report":
            print(f'Water: {menu.resources["water"]}')
            print(f'Milk: {menu.resources["milk"]}')
            print(f'Coffee: {menu.resources["coffee"]}')
            print(f'Money: {menu.resources["money"]}')
        elif coffeeAsk == "espresso":
            print(f'The price of a espresso is ${menu.hot_Coffee["espresso"]["price"]}')
            print("Please insert your coins")
            total = moneyInput()
            makeCoffee(coffeeAsk)
        elif coffeeAsk == "latte":
            print(f'The price of a latte is ${menu.hot_Coffee["latte"]["price"]}')
            print("Please insert your coins")
            total = moneyInput()
            makeCoffee(coffeeAsk)
        elif coffeeAsk == "cappuccino":
            print(f'The price of a cappuccino is ${menu.hot_Coffee["cappuccino"]["price"]}')
            print("Please insert your coins")
            total = moneyInput()
            makeCoffee(coffeeAsk)
        elif coffeeAsk == "exit":
            print("Thanks for using our machine!")
            on = False
       

coffeeMaker()