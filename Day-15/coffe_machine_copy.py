from coffe_machine_menu_data import menu, resources
profit = 0
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee :{coffee}g\nprofit: {profit}")
def check_resource(drink):
    drink_ingreidents = menu[drink]["ingredients"]
    for item in drink_ingreidents:
        if resources[item] < drink_ingreidents[item]:
            print(f"Sorry not enough {item}.")
            return False
    return True
def money_process():
    print("please insert money in rupees.")
    take_money = int(input("How many rupees?₨: "))
    return take_money
def is_transction_successfull(take_money, drink_price):
    if take_money >= drink_price:
        global profit
        change = round(take_money - drink_price, 2)
        print(f"Here is your ₨{change} in change.")
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money.")
def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"here is Your {drink_name} coffee.")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        drink = menu[choice]
        is_resuource_available = check_resource(choice)
        if is_resuource_available:
            payment = money_process()
            if is_transction_successfull(payment, drink["cost"]):
                make_coffee()


            
