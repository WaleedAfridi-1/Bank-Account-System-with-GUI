import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
        self.__transactions = []

    def withdraw(self, amount):
        if self.__balance < amount:
            return "Insufficient balance!"
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdraw: Rs.{amount}")
            return f"Rs.{amount} Withdrawn Successfully."

    def deposit(self, amount):
        if amount < 0:
            return "Error! Please enter a valid amount."
        else:
            self.__balance += amount
            self.__transactions.append(f"Deposit: Rs.{amount}")
            return f"Rs.{amount} Deposited Successfully."

    def check_balance(self):
        return f"Your current balance is Rs.{self.__balance}"

    def transaction_history(self):
        return self.__transactions[-5:][::-1]


# ---------------- GUI CODE ---------------- #
account = BankAccount()

def deposit_amount():
    try:
        amount = int(entry_amount.get())
        result = account.deposit(amount)
        messagebox.showinfo("Deposit", result)
    except:
        messagebox.showerror("Error", "Please enter a valid amount.")

def withdraw_amount():
    try:
        amount = int(entry_amount.get())
        result = account.withdraw(amount)
        messagebox.showinfo("Withdraw", result)
    except:
        messagebox.showerror("Error", "Please enter a valid amount.")

def check_balance():
    result = account.check_balance()
    messagebox.showinfo("Balance", result)

def show_transactions():
    transactions = account.transaction_history()
    history = "\n".join(transactions) if transactions else "No transactions yet."
    messagebox.showinfo("Transaction History", history)

# --- Tkinter Window --- #
win = tk.Tk()
win.title("Bank Account System")
win.geometry("350x300")

label = tk.Label(win, text="Enter Amount (Rs):")
label.pack(pady=10)

entry_amount = tk.Entry(win)
entry_amount.pack()

btn_deposit = tk.Button(win, text="Deposit", width=20, command=deposit_amount)
btn_deposit.pack(pady=5)

btn_withdraw = tk.Button(win, text="Withdraw", width=20, command=withdraw_amount)
btn_withdraw.pack(pady=5)

btn_balance = tk.Button(win, text="Check Balance", width=20, command=check_balance)
btn_balance.pack(pady=5)

btn_history = tk.Button(win, text="Transaction History", width=20, command=show_transactions)
btn_history.pack(pady=5)

btn_exit = tk.Button(win, text="Exit", width=20, command=win.quit)
btn_exit.pack(pady=10)

win.mainloop()
