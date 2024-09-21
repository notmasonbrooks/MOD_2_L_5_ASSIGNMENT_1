# my functions are highlighted with the message "missing function". The function works as intended and the warning seems to have no effect on the program.


def add_numbers(a, b):
    total_sum = a + b
    print(total_sum)
    return total_sum


def sub_numbers(a, b):
    total_sub = a - b
    return total_sub


def mul_numbers(a, b):
    total_mul = a * b
    return total_mul


def div_numbers(a, b):
    try:
        total_div = a / b
    except ZeroDivisionError:
        total_div = 0
    return total_div


while True:
    print("-The Calculator App-")
    print("Would you like to:")
    print("[A]dd")
    print("[S]ubtract")
    print("[M]ultiply")
    print("[D]ivide")
    print("[Q]uit")
    choice = input("").upper()
    if choice == "A":
        num1 = int(input("Enter your first number:\n"))
        num2 = int(input("Enter your second number:\n"))
        print(f"{num1} + {num2} = {add_numbers(num1, num2)}")
    elif choice == "S":
        num1 = int(input("Enter your first number:\n"))
        num2 = int(input("Enter your second number:\n"))
        print(f"{num1} - {num2} = {sub_numbers(num1, num2)}")
    elif choice == "M":
        num1 = int(input("Enter your first number:\n"))
        num2 = int(input("Enter your second number:\n"))
        print(f"{num1} * {num2} = {mul_numbers(num1, num2)}")
    elif choice == "D":
        num1 = int(input("Enter your first number:\n"))
        num2 = int(input("Enter your second number:\n"))
        print(f"{num1} / {num2} = {div_numbers(num1, num2):.2f}")
    elif choice == "Q":
        break
    else:
        print("Invalid input.")
