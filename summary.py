from utlis import format_rupiah
import matplotlib.pyplot as plt

def show_summary(data):
    income = sum(t['amount'] for t in data if t['amount'] > 0)
    expense = sum(t['amount'] for t in data if t['amount'] < 0)
    balance = income + expense

    print("\n=== Financial Summary ===")
    print(f"Total Income     : {format_rupiah(income)}")
    print(f"Total Expenses   : {format_rupiah(abs(expense))}")
    print(f"Current Balance  : {format_rupiah(balance)}")

    
    # Prevent chart generation if there is no data
    if income == 0 and expense == 0:
        print("\nNo data to visualize.")
        return

    # Panggil fungsi visualisasi
    visualize_summary(income, abs(expense))

def visualize_summary(income, expense):
    # Data untuk pie chart
    labels = 'Income', 'Expenses'
    sizes = [income, expense]
    colors = ['#66b3ff', '#ff9999']  # Biru untuk pemasukan, merah untuk pengeluaran
    explode = (0.1, 0)  # "Meledakkan" irisan pemasukan sedikit

    # Membuat pie chart
    plt.figure(figsize=(8, 6))  # Ukuran chart
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
            shadow=True, startangle=90)
    plt.title('Income vs Expenses', fontsize=16)
    plt.axis('equal')  # Membuat lingkaran sempurna

    # Menampilkan chart
    plt.show()
