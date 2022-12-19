import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation (+, -, *, /): ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            clear_screen()
            print(logo)
            num1 = answer
            print(f"The first number is: {num1}")
        else:
            should_continue = False
            clear_screen()
            calculator()

calculator()
