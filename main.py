def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    first_number = int(input("please enter first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        symbol_pick = input("enter the symbol you want to apply: ")
        next_number = int(input("please enter next number: "))
        calculation = operations[symbol_pick]
        answer = calculation(first_number, next_number)
        print(f"{first_number} {symbol_pick} {next_number} = {answer}")
        if input("do you want to continue with this number? type 'y' to continue type 'n' to reset.") == "y":
            first_number = answer

        else:
            should_continue = False
            calculate()


calculate()

