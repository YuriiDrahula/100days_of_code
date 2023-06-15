from logo import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    a = float(input("What's the first number: "))
    for operation in operations:
        print(operation)

    run_calculator = True
    while run_calculator:
        pick_operation = input("Pick an operation: ")
        b = float(input("What's the next number: "))

        result = operations[pick_operation](a, b)
        print(f"{a} {pick_operation} {b} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ")
        if choice == "y":
            a = result
        else:
            run_calculator = False
            calculator()


calculator()

