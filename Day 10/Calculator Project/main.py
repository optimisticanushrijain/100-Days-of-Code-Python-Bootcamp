import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calc():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    while should_accumulate:
        for keys in calculator:
            print(keys)
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = calculator[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calc()

calc()