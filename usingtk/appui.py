import tkinter as tk
from tkinter import messagebox
from banking import SavingsAccount, CheckingAccount, InsufficientFundsError

# Global dictionary to store accounts
accounts = {}

# Function to create an account
def create_account():
    account_number = entry_acc_num.get()
    account_holder = entry_acc_holder.get()
    account_type = account_type_var.get()
    initial_balance = float(entry_initial_balance.get())

    if account_type == "Savings":
        interest_rate = float(entry_interest_rate.get())
        accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
    else:
        accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)

    messagebox.showinfo("Success", f"Account {account_number} created successfully!")

# Function to deposit money
def deposit_money():
    account_number = entry_deposit_acc.get()
    amount = float(entry_deposit_amount.get())

    if account_number in accounts:
        accounts[account_number].deposit(amount)
        messagebox.showinfo("Success", f"Deposited {amount}. New balance: {accounts[account_number].get_balance()}")
    else:
        messagebox.showerror("Error", "Account not found!")

# Function to withdraw money
def withdraw_money():
    account_number = entry_withdraw_acc.get()
    amount = float(entry_withdraw_amount.get())

    if account_number in accounts:
        try:
            accounts[account_number].withdraw(amount)
            messagebox.showinfo("Success", f"Withdrew {amount}. New balance: {accounts[account_number].get_balance()}")
        except InsufficientFundsError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Account not found!")

# Function to check balance
def check_balance():
    account_number = entry_balance_acc.get()

    if account_number in accounts:
        messagebox.showinfo("Balance Info", f"Balance: {accounts[account_number].get_balance()}")
    else:
        messagebox.showerror("Error", "Account not found!")

# Main GUI
root = tk.Tk()
root.title("Banking System")

# Account Creation Section
frame_create = tk.LabelFrame(root, text="Create Account")
frame_create.pack(pady=10)

tk.Label(frame_create, text="Account Number:").grid(row=0, column=0)
entry_acc_num = tk.Entry(frame_create)
entry_acc_num.grid(row=0, column=1)

tk.Label(frame_create, text="Account Holder:").grid(row=1, column=0)
entry_acc_holder = tk.Entry(frame_create)
entry_acc_holder.grid(row=1, column=1)

tk.Label(frame_create, text="Account Type:").grid(row=2, column=0)
account_type_var = tk.StringVar(value="Savings")
tk.Radiobutton(frame_create, text="Savings", variable=account_type_var, value="Savings").grid(row=2, column=1)
tk.Radiobutton(frame_create, text="Checking", variable=account_type_var, value="Checking").grid(row=2, column=2)

tk.Label(frame_create, text="Initial Balance:").grid(row=3, column=0)
entry_initial_balance = tk.Entry(frame_create)
entry_initial_balance.grid(row=3, column=1)

tk.Label(frame_create, text="Interest Rate (Savings Only):").grid(row=4, column=0)
entry_interest_rate = tk.Entry(frame_create)
entry_interest_rate.grid(row=4, column=1)

tk.Button(frame_create, text="Create Account", command=create_account).grid(row=5, columnspan=2)

# Deposit Money Section
frame_deposit = tk.LabelFrame(root, text="Deposit Money")
frame_deposit.pack(pady=10)

tk.Label(frame_deposit, text="Account Number:").grid(row=0, column=0)
entry_deposit_acc = tk.Entry(frame_deposit)
entry_deposit_acc.grid(row=0, column=1)

tk.Label(frame_deposit, text="Amount:").grid(row=1, column=0)
entry_deposit_amount = tk.Entry(frame_deposit)
entry_deposit_amount.grid(row=1, column=1)

tk.Button(frame_deposit, text="Deposit", command=deposit_money).grid(row=2, columnspan=2)

# Withdraw Money Section
frame_withdraw = tk.LabelFrame(root, text="Withdraw Money")
frame_withdraw.pack(pady=10)

tk.Label(frame_withdraw, text="Account Number:").grid(row=0, column=0)
entry_withdraw_acc = tk.Entry(frame_withdraw)
entry_withdraw_acc.grid(row=0, column=1)

tk.Label(frame_withdraw, text="Amount:").grid(row=1, column=0)
entry_withdraw_amount = tk.Entry(frame_withdraw)
entry_withdraw_amount.grid(row=1, column=1)

tk.Button(frame_withdraw, text="Withdraw", command=withdraw_money).grid(row=2, columnspan=2)

# Check Balance Section
frame_balance = tk.LabelFrame(root, text="Check Balance")
frame_balance.pack(pady=10)

tk.Label(frame_balance, text="Account Number:").grid(row=0, column=0)
entry_balance_acc = tk.Entry(frame_balance)
entry_balance_acc.grid(row=0, column=1)

tk.Button(frame_balance, text="Check Balance", command=check_balance).grid(row=1, columnspan=2)

root.mainloop()
