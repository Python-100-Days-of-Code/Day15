import os
from dictionary import menu, resources


# TODO 3. Get Payment
def get_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickels = int(input("How many nickels ?: "))
    pennies = int(input("How many pennies ?: "))

    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


# TODO 2. Check Resources - **Note** no milk for Espresso
def check_resource(drink):
    if resources["water"] - menu[drink]["ingredients"]["water"] < 0:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] - menu[drink]["ingredients"]["coffee"] < 0:
        print("Sorry there is not enough coffee.")
        return False
    elif drink != "espresso":
        if resources["milk"] - menu[drink]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            return False
    return True


# TODO 4. Make Coffee
def make_coffee(drink):
    resources["water"] -= menu[drink]["ingredients"]["water"]
    resources["coffee"] -= menu[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= menu[drink]["ingredients"]["milk"]


# TODO 6. Print Report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${cash}")


os.system("clear")
cash = 0
not_turn_off = True

while not_turn_off:
    # TODO: 1. Ask user
    drink = input("What would you like? (espresso/latte/cappuccino):")
    if drink == "off":
        not_turn_off = False
    elif drink == "report":
        print_report()
    else:
        if check_resource(drink):
            payment = round(get_payment(), 2)
            cost = float(menu[drink]["cost"])

            if payment >= cost:
                make_coffee(drink)

                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change")

                # TODO 5. Update Cash
                cash += cost

                print(f"Here is your {drink} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    # Space between runs
    print("\n")
