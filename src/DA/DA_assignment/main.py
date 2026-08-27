from preprocessing import (
    read_data_file,
    drop_cols,
    check_data_type
)

from config.config import COLS_TO_DROP


def show_menu() -> None:
    """
    Display the available preprocessing options.
    """
    print("\n" + "=" * 40)
    print("     PREPROCESSING SYSTEM")
    print("=" * 40)
    print("1. Read Dataset")
    print("2. Remove Unnecessary Columns")
    print("3. Check Data Types")
    print("4. Run Complete Pipeline")
    print("5. Exit")
    print("=" * 40)


def ask_to_continue() -> bool:
    """
    Ask the user whether they want to continue.

    Returns:
        bool: True if the user wants to continue,
        False if the user wants to exit.
    """
    while True:
        choice = input("\nDo you want to continue? (yes/no): ").strip().lower()

        if choice in ["yes", "y"]:
            return True

        if choice in ["no", "n"]:
            return False

        print("Invalid input. Please enter yes or no.")


def main() -> None:
    """
    Run the Titanic preprocessing system.
    """
    file_path: str = "data/raw/Titanic.csv"
    df = None

    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        # Option 1: Read dataset
        if choice == "1":
            df = read_data_file(file_path)

            if df is not None:
                print("\nDataset loaded successfully.")
                print("\nFirst 5 rows:")
                print(df.head())

        # Option 2: Drop columns
        elif choice == "2":
            if df is None:
                print("\nPlease read the dataset first.")

            else:
                df = drop_cols(df, COLS_TO_DROP)
                print("\nColumns removed successfully.")
                print("Remaining columns:")
                print(df.columns.tolist())

        # Option 3: Check data types
        elif choice == "3":
            if df is None:
                print("\nPlease read the dataset first.")

            else:
                report = check_data_type(df)
                print("\nData Quality Report:")
                print(report)

        # Option 4: Complete pipeline
        elif choice == "4":
            df = read_data_file(file_path)

            if df is not None:
                df = drop_cols(df, COLS_TO_DROP)

                report = check_data_type(df)

                print("\nComplete pipeline finished successfully.")
                print("\nData Quality Report:")
                print(report)

        # Option 5: Exit
        elif choice == "5":
            print("\nThank you for using the Preprocessing System. Goodbye!")
            break

        # Invalid choice
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")
            continue

        # Ask user whether to continue
        if not ask_to_continue():
            print("\nThank you for using the Preprocessing System. Goodbye!")
            break


if __name__ == "__main__":
    main()