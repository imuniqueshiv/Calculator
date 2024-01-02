# Import the logo from the art module
from art import logo

# Define arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary to map operation symbols to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator function
def calculator():
    # Display the logo
    print(logo)

    # Get the first number from the user
    num1 = float(input("Enter first number: "))

    # Display available operations
    for symbol in operations:
        print(symbol)

    # Variable to control the loop
    should_continue = True

    # Start a loop to allow the user to perform calculations
    while should_continue:
        # Get the operation symbol from the user
        operation_symbol = input("Pick an operation from the line above: ")
        
        # Get the second number from the user
        num2 = float(input("Enter second number: "))

        # Perform the calculation based on the user's input
        calculation_fun = operations[operation_symbol]
        answer = calculation_fun(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue with the result or start a new calculation
        if input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()  # Recursively call the calculator function for a new calculation

# Start the calculator
calculator()
