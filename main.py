from classes import Account, CurrentAccount, DepositAccount, RestrictedAccount, AccountWithOverdraft, Bank

def create_account():
    account_type = input("Enter account type (current, deposit, restricted, overdraft): ").strip().lower()
    name = input("Enter account holder's name: ").strip()
    account_number = input("Enter account number: ").strip()
    balance = float(input("Enter initial balance: ").strip())

    if account_type == "current":
        return CurrentAccount(name, account_number, balance)
    elif account_type == "deposit":
        interest_rate = float(input("Enter interest rate (as a decimal): ").strip())
        withdrawals_limit = int(input("Enter withdrawal limit: ").strip())
        return DepositAccount(name, account_number, balance, interest_rate, withdrawals_limit)
    elif account_type == "restricted":
        max_withdrawal_limit = float(input("Enter maximum withdrawal limit: ").strip())
        return RestrictedAccount(name, account_number, balance, max_withdrawal_limit)
    elif account_type == "overdraft":
        overdraft_limit = float(input("Enter overdraft limit: ").strip())
        return AccountWithOverdraft(name, account_number, balance, overdraft_limit)
    else:
        print("Invalid account type!")
        return None

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Withdraw from Account")
        print("3. Deposit to Account")
        print("4. Apply Interest to Deposit Accounts")
        print("5. Save Accounts to File")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            account = create_account()
            if account:
                bank.add_account(account)
                print("Account created successfully!")
        elif choice == '2':
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount to withdraw: ").strip())
            print(bank.withdraw_from_account(account_number, amount))
        elif choice == '3':
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount to deposit: ").strip())
            print(bank.deposit_to_account(account_number, amount))
        elif choice == '4':
            bank.apply_interest_to_deposit_accounts()
        elif choice == '5':
            filename = input("Enter filename to save accounts: ").strip()
            bank.save_accounts(filename)
            print("Accounts saved successfully!")
        elif choice == '6':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
