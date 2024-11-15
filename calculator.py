from art import logo

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
    "/": divide,
}

def calculator_():
    print(logo)
    continue_ = True
    num1 = float(input("Enter the first number: "))

    while continue_:
        # Display available operators
        for symbol in operations:
            print(symbol)

        # Get operator from user
        operator = input("Choose an operator (+, -, *, /): ")

        # Get second number from user
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        # Ask user if they want to continue with the result or start a new calculation
        choice = input(f"Enter 'Y' to continue calculation with {answer} "
                       f"or 'N' for a new calculation "
                       f"or 'X' to exit: ").lower()

        # Update num1 for continued calculations
        if choice == "y":
            num1 = answer
        # End current loop and start a new calculation
        elif choice == "n":
            continue_ = False
            print("\n" * 20)  # Clear the screen
            calculator_()
        # Exit the loop
        else:
            continue_ = False

# Start the calculator
calculator_()
