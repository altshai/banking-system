import streamlit as st
from banking import SavingsAccount, CheckingAccount, InsufficientFundsError

# Initialize session state for accounts
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

st.title("Banking System")

menu = st.sidebar.radio("Menu", ["Create Account", "Deposit", "Withdraw", "Transfer Money", "Calculate Interest", "View Account Info"])

if menu == "Create Account":
    st.subheader("Create a New Account")
    account_number = st.text_input("Account Number")
    account_holder = st.text_input("Account Holder Name")
    account_type = st.selectbox("Account Type", ["Savings", "Checking"])
    initial_balance = st.number_input("Initial Balance", min_value=0.0)

    if account_type == "Savings":
        interest_rate = st.number_input("Interest Rate (e.g., 0.01 for 1%)", min_value=0.0, max_value=1.0, value=0.01)
    else:
        interest_rate = None

    if st.button("Create Account"):
        if account_number and account_holder:
            if account_type == "Savings":
                st.session_state.accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
            else:
                st.session_state.accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)
            st.success("Account created successfully!")
        else:
            st.error("Please fill in all fields.")

elif menu == "Deposit":
    st.subheader("Deposit Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Deposit Amount", min_value=0.0)

    if st.button("Deposit"):
        if account_number in st.session_state.accounts:
            st.session_state.accounts[account_number].deposit(amount)
            st.success(f"Deposited {amount}. New balance: {st.session_state.accounts[account_number].get_balance()}")
        else:
            st.error("Account not found!")

elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Withdraw Amount", min_value=0.0)

    if st.button("Withdraw"):
        if account_number in st.session_state.accounts:
            try:
                st.session_state.accounts[account_number].withdraw(amount)
                st.success(f"Withdrew {amount}. New balance: {st.session_state.accounts[account_number].get_balance()}")
            except InsufficientFundsError as e:
                st.error(str(e))
        else:
            st.error("Account not found!")

elif menu == "Transfer Money":
    st.subheader("Transfer Money")
    from_account = st.text_input("From Account")
    to_account = st.text_input("To Account")
    amount = st.number_input("Transfer Amount", min_value=0.0)

    if st.button("Transfer"):
        if from_account in st.session_state.accounts and to_account in st.session_state.accounts:
            try:
                st.session_state.accounts[from_account].withdraw(amount)
                st.session_state.accounts[to_account].deposit(amount)
                st.success("Transfer successful!")
            except InsufficientFundsError as e:
                st.error(str(e))
        else:
            st.error("One or both accounts not found!")

elif menu == "Calculate Interest":
    st.subheader("Calculate Interest (Savings Accounts Only)")
    account_number = st.text_input("Account Number")

    if st.button("Calculate"):
        if account_number in st.session_state.accounts:
            if isinstance(st.session_state.accounts[account_number], SavingsAccount):
                interest = st.session_state.accounts[account_number].calculate_interest()
                st.success(f"Interest added: {interest}. New balance: {st.session_state.accounts[account_number].get_balance()}")
            else:
                st.error("Interest calculation is only for savings accounts!")
        else:
            st.error("Account not found!")

elif menu == "View Account Info":
    st.subheader("View Account Information")
    account_number = st.text_input("Account Number")

    if st.button("View"):
        if account_number in st.session_state.accounts:
            st.info(st.session_state.accounts[account_number].display_account_info())
        else:
            st.error("Account not found!")
