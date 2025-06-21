def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def format_rupiah(amount):
    return f"Rp {amount:,.2f}"

def input_menu(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("Invalid choice. Please choose from", options)

def convert_usd_to_idr(amount_usd):
    exchange_rate = 15500.0 
    return amount_usd * exchange_rate

