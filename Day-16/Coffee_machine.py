# coffee machine
from coffeemaker_data import CoffeeMaker, Menu, MenuItem, MoneyMachine
money_machine = MoneyMachine()
coffee_Maker = CoffeeMaker()
menu = Menu()

machine_on = True
while machine_on:
    opitions = menu.get_items()
    choice = input(f"What would you like? ({opitions}): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_Maker.report()
        money_machine.report() 
    else:
        drink = menu.find_drink(choice)
        is_drink_available = coffee_Maker.is_resource_sufficient(drink)
        if is_drink_available and money_machine.make_payment(drink.cost):
            coffee_Maker.make_coffee(drink) 