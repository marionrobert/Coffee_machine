coffees_with_prices = {"Espresso": 1.50, "Latte": 2.50, "Cappuccino": 3.00}
machine_resources = {"Water": 1000, "Milk": 500, "Coffee": 500, "Money": 0}
menu = {"Espresso": {"Water": 50, "Coffee": 18, "Milk": 0}, "Latte": {"Water": 200, "Coffee": 24, "Milk": 150}, "Cappuccino": {"Water": 250, "Coffee": 24, "Milk": 100}}


def is_enough_resources(coffee):
    if machine_resources["Water"] >= menu[coffee]["Water"]:
        if machine_resources["Milk"] >= menu[coffee]["Milk"]:
            if machine_resources["Coffee"] >= menu[coffee]["Coffee"]:
                return True
            else:
                print("Sorry, there is not enough coffee.")
                return False
        else:
            print("Sorry, there is not enough milk.")
            return False
    else:
        print("Sorry, there is not enough water.")
        return False


def reduce_resources(coffee):
    for ingredient in menu[coffee]:
        machine_resources[ingredient] -= menu[coffee][ingredient]


def calculate_total_inserted(nb_quarters, nb_dimes, nb_nickles, nb_pennies):
    total = nb_quarters * 0.25 + nb_dimes * 0.1 + nb_nickles * 0.05 + nb_pennies * 0.01
    return total


def is_enough_money(money_inserted, coffee):
    if money_inserted > coffees_with_prices[coffee]:
        return True


def make_transaction(money_inserted, coffee):
    # add total to machine_resources
    machine_resources["Money"] += round(total, 2)
    # calculate and return change
    return round(money_inserted - coffees_with_prices[coffee], 2)


machine_on = True

while machine_on:
    client_choice = input("What would you like? (espresso/latte/cappuccino): ").capitalize()

    if client_choice == "Off":
        print("Machine turned off.")
        machine_on = False

    elif client_choice == "Report":
        print(f"Water: {machine_resources['Water']}ml \nMilk: {machine_resources['Milk']}ml\nCoffee: {machine_resources['Coffee']}g \nMoney: ${machine_resources['Money']}")

    elif client_choice in coffees_with_prices:
        if is_enough_resources(client_choice):
            print(f"please, insert coins for : ${coffees_with_prices[client_choice]}")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total = calculate_total_inserted(quarters, dimes, nickles, pennies)
            if is_enough_money(total, client_choice):
                change = make_transaction(total, client_choice)
                print(f"Thanks, here is {change} dollars in change.")
                reduce_resources(client_choice)
                print(f"Here is your {client_choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.”")

        else:
            print("We can't make your coffee. Try to order something else.")