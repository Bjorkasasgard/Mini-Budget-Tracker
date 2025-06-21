from transaction import add_transaction, show_transactions, delete_transaction, edit_transaction
from summary import show_summary
from file_handler import load_data, save_data

def show_user_guide():
    guide_text = """ 
    =======================================================================
                    Welcome to the Mini Budget Tracker!
    =======================================================================

    This application is designed to help you easily and quickly track and 
    manage your personal finances.

    HOW TO USE:
    Select an option from the menu by typing the corresponding number, 
    then press Enter.

    FEATURE EXPLANATIONS:
    1. Add Transaction:
       - Record a new income or expense.
       - Use a positive number (e.g., 50000) for INCOME.
       - Use a negative number (e.g., -15000) for an EXPENSE.
       - You can enter the amount in IDR or USD.

    2. Show All Transactions:
       - Displays a complete list of your transaction history.

    3. Edit Transaction:
        - Midify the details of an existing transaction.

    4. Delete Transaction:
       - Removes a transaction based on its list number.

    5. Show Financial Summary:
       - Provides a summary of total income, expenses, your final balance,
         and a pie chart visualization.

    6. Save & Exit:
       - IMPORTANT! Use this to exit and save all your data.

    Want the code for this program? Check out my GitHub:
    GitHub: https://github.com/Bjorkasasgard/Mini-Budget-Tracker 
    For Feedback:
    Email: adam.bastian_ti24@nusaputra.ac.id
    =======================================================================
    """
    print(guide_text)
    input("--> Press Enter to continue to the main menu...")

def main():   
    data = load_data()
    show_user_guide()
    while True:
        print("\n=== Mini Budget Tracker ===")
        print("1. Add Transaction ")
        print("2. Show All Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Show Financial Summary")
        print("6. Save & Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            show_transactions(data)
        elif choice == "3":
            edit_transaction(data)
        elif choice == "4":
            delete_transaction(data)
        elif choice == "5":
            show_summary(data)
        elif choice == "6":
            save_data(data)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
