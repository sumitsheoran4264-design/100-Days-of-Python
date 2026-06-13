#calculator 
calculator_art ='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

(Calculator)'''
print(calculator_art)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():                  # We make this function becasue when the user type n the calculator reset from new vaues(num1 and num2).
    should_accumlate = True
    num1 = float(input("What was the first number?: "))
    while should_accumlate :

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick one operation: ")
        num2 = float(input("What was the next number?: "))
        result = operations[operation_symbol](n1=num1, n2=num2)
        print(f"{num1} {operation_symbol} {num2} = {result}") # example 2 + 2 = 4.0

        continue_calculating = input(f"Type 'y' for continue with {result}, or type 'n' for new calculation: ").lower()
        if continue_calculating == 'y':
            num1 = result    
        else:
            should_accumlate = False
            print("\n" * 100)
            calculator() #restarts the calculator when needed

calculator() #starts the calculator