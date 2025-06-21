
from utlis import convert_usd_to_idr, input_float, format_rupiah
def add_transaction(data):
    try:
        description = input("Description: ")
        currency_choice = input("Enter currency (1 for IDR, 2 for USD): ")
        raw_amount = input_float("Amount (use negative for expense): ")

        if currency_choice == "2":
            amount = convert_usd_to_idr(raw_amount)
            print(f"Converted to Rupiah: {format_rupiah(amount)}")

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


def delete_transaction(data):
    show_transactions(data)
    try:
        index = int(input("Enter transaction number to -delete: ")) - 1
        if 0 <= index < len(data):
            del data[index]
            print("Transaction deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")
