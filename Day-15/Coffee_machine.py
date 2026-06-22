#import data 
from coffe_machine_menu_data import menu, resources
profit = 0
def print_report():
        '''if user type report show him resources'''
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}"

def check_resources(drink):
     '''This function check resource of drink and return (True or False)'''
     drink_ingredients = menu[drink]["ingredients"]
     for item in drink_ingredients:
          if resources[item] < drink_ingredients[item]:
                print(f"Sorry, not enough {item}")
                return False
          
     return True


def coin_process():
     "return the total calculated from coins inserted."
     print("please insert coins")
     total = int(input("How many quarters?: ")) * 0.25
     total += int(input("How many dimes?: ")) * 0.1
     total += int(input("how many nickeles?: " )) * 0.05
     total += int(input("How many pennies?: ")) * 0.01
     return total

def is_transaction_successful(money_recived, drink_cost):
     '''return true when the payment is accepted, or False if money is insuffincient.'''
     if money_recived >= drink_cost:
          global profit
          change = round(money_recived - drink_cost, 2)
          print(f"Here is ${change} in change.")
          profit += drink_cost
          return True
     else:
          print("Sorry, that's not enough money. Money refunded.")
          return False
def make_coffe(drink_name, drink_ingredients):
     "Deduct the required ingredients from the resources."
     for item in drink_ingredients:
          resources[item] -= drink_ingredients[item]
     print(f"Here is your {drink_name} coffee.")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
         machine_on = False
    elif choice == "report":
        print(print_report())
    else:
         drink = menu[choice]
         is_drink_available = check_resources(choice)
         if is_drink_available:
               payment = coin_process()
               if is_transaction_successful(payment, drink['cost']):
                    make_coffe(choice, drink["ingredients"])



         

    