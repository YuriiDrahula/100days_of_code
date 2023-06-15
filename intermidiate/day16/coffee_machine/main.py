from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        ordered_coffe = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(ordered_coffe):
            if money_machine.make_payment(ordered_coffe.cost):
                coffee_maker.make_coffee(ordered_coffe)
