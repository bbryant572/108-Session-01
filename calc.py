"""
Calc
Simple python calculator
Brett Bryant
"""
# imports


# global vars


# functions

def print_header():
    print("-" * 25)
    print(" PyCalc 3000 ")
    print("-" * 25)

    print("[1] - Sum")
    print("[2] - Substract")
    print("[3] - Multiplication")
    print("[4] - Division")

    print("[5] - Repeat Message")

    print("[q] - Quit")


# plain instructions
option = ""
while(option != "q"):
    print_header()

    option = input("Select an option: ")
    if option == "q":
        break  # end the loop

    if option == "5":
        message = input("Enter message here: ")
        num3 = int(input("How many times to repeat? "))
        res = ((message + " ") * num3)
        print(res)
    else:
        num1 = float(input("Please select num1: "))
        num2 = float(input("Please select num2: "))

    if option == "1":
        res = num1 + num2
        print("The result is: " + str(res))

    if option == "2":
        res = num1 - num2
        print("The result is: " + str(res))

    if option == "3":
        res = num1 * num2
        print("The result is: " + str(res))

    if option == "4":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            res = num1 / num2
            print("The result is: " + str(res))

    input("Press enter to continue...")

print("Good Bye!")
