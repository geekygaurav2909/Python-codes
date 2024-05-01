#Addition
def add(n1, n2):
    return n1+n2

#Subtraction
def sub(n1, n2):
    return n1-n2

#Multiplication
def mul(n1, n2):
    return n1*n2

#Division
def div(n1, n2):
    return n1/n2


calc_dictionary = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

from day10_calculator_logo import logo
def calculator():
    print(logo)
    num1 = float(input("What's your first number?: "))
    for operations in calc_dictionary:
        print(operations)
    more_operation = True
    while more_operation:
        choose_symbol = input("Pick an operation: ")
        num2 = float(input("What's next number?: "))
        first_answer = calc_dictionary[choose_symbol](num1, num2)
        print(f"{num1} {choose_symbol} {num2} = {first_answer}")

        wants_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ").lower()

        if wants_continue == 'y':
            num1 = first_answer
        elif wants_continue == 'n':
            more_operation = False
            calculator()

calculator()




