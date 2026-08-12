from calculator import add, subtract, multiply, divide
from ui import show_menu, get_numbers


def main():
    print("Welcome to the Simple Calculator!")

    while True:
        show_menu()

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

            if result is None:
                print("Cannot divide by zero.")
                continue

        print("Result:", result)

        again = input("Do you want to perform another calculation? (yes/no): ")

        if again.lower() == "no":
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()