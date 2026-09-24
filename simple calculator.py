def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


while True:
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", addition(num1, num2))

            elif choice == "2":
                print("Result:", subtraction(num1, num2))

            elif choice == "3":
                print("Result:", multiplication(num1, num2))

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", division(num1, num2))

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Invalid choice. Please select 1 to 5.")