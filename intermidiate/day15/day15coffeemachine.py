from menu import MENU, resources
from emoji import emojize

money = 0


def recourses():
    """Returns String of the current resources and profit amount"""
    return f'''Water: {resources["water"]}ml
    \rMilk: {resources["milk"]}ml
    \rCoffee: {resources["coffee"]}
    \rMoney: ${money}'''


def is_resources_sufficient(drink):
    """Take the drink name adn returns True if there is enough ingredients and False if ingredients are insufficient"""
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print(f"Sorry there is not enough water")
        return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print(f"Sorry there is not enough coffee")
        return False
    else:
        return True


def process_coins():
    """Returns the total calculated coins"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.02
    pennies = int(input("how many pennies?: ")) * 0.01
    sum_of_coins = quarters + dimes + nickles + pennies
    return round(sum_of_coins, 2)


def is_transaction_successful(inserted_coins, chosen_drink):
    """Takes inserted coins and drink name, compares them with the cost of the drink
    and returns False if inserted coins are less than the drink value and True if enough"""
    global money
    if inserted_coins < MENU[chosen_drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_coins == MENU[chosen_drink]["cost"]:
        money += inserted_coins
        return True
    elif inserted_coins > MENU[chosen_drink]["cost"]:
        money += MENU[chosen_drink]["cost"]
        change = inserted_coins - MENU[chosen_drink]["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def make_coffe(chosen_coffee):
    global resources
    if chosen_coffee != "espresso":
        resources["water"] -= MENU[chosen_coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[chosen_coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[chosen_coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[chosen_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[chosen_coffee]["ingredients"]["coffee"]

    for coffee in MENU:
        if coffee == chosen_coffee:
            print(emojize(f"Here is your {coffee} :brown_heart: Enjoy!"))


coffee_machine_running = True
while coffee_machine_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    chosen_coffee = user_choice
    if chosen_coffee == "espresso"\
        or chosen_coffee == "latte"\
        or chosen_coffee == "cappuccino":
        is_sufficient = is_resources_sufficient(chosen_coffee)
        if is_sufficient:
            inserted_coins = process_coins()
            if is_transaction_successful(inserted_coins, chosen_coffee):
                make_coffe(chosen_coffee)
    elif user_choice == "report":
        print(recourses())
    elif user_choice == "off":
        coffee_machine_running = False
