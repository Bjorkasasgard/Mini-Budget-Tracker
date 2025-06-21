from utlis import convert_usd_to_idr, input_float, format_rupiah, input_menu
def add_transaction(data):
    try:
        description = input("Description: ")

        currency_choice = input_menu("Enter currency (1 for IDR, 2 for USD): ", ["1", "2"])
        raw_amount = input_float("Amount (use negative for expense): ")
           
        if currency_choice == "2":
            amount = convert_usd_to_idr(raw_amount)

        else:
            amount = raw_amount

        category = input("Category (e.g., Food, Salary, Transport): ")
        transaction = {
            "description": description,
            "amount": amount,
            "category": category
        }
        data.append(transaction)
        print("Transaction in IDR added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_transactions(data):
    if not data:
        print("No transactions available.")
        return
    for i, t in enumerate(data):
        status = "Income" if t["amount"] > 0 else "Expense"
        print(f"{i+1}. {t['description']} - {format_rupiah(t['amount'])} ({status}) | Category: {t['category']}")

def edit_transaction(data):
    show_transactions(data)
    if not data:
        return

    try:
        index_str = input("Enter the number of the transaction to edit (or 0 to cancel): ")
        index = int(index_str) - 1

        if index == -1: # User chose 0 to cancel
            print("Edit cancelled.")
            return

        if not (0 <= index < len(data)):
            print("Invalid transaction number.")
            return

        transaction = data[index]
        print(f"\n--- Editing Transaction #{index + 1} ---")
        print(f"1. Description: {transaction['description']}")
        print(f"2. Amount     : {format_rupiah(transaction['amount'])}")
        print(f"3. Category   : {transaction['category']}")
        
        choice = input_menu("Choose a field to edit (1-3, or press Enter to cancel): ", ["1", "2", "3", ""])

        if choice == "1":
            transaction['description'] = input("Enter new description: ")
        elif choice == "2":
            print("Note: Please enter the new amount in IDR.")
            transaction['amount'] = input_float("Enter new amount (use negative for expense): ")
        elif choice == "3":
            transaction['category'] = input("Enter new category: ")
        
        if choice: # Only print if an edit was made
            print("Transaction updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_transaction(data):
    show_transactions(data)
    try:
        index = int(input("Enter transaction number to delete: ")) - 1
        if 0 <= index < len(data):
            del data[index]
            print("Transaction deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")
