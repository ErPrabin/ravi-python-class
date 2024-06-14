from classes import Account, CurrentAccount, DepositAccount, RestrictedAccount, AccountWithOverdraft, Bank

if __name__ == "__main__":
    # Create a bank
    bank = Bank()

    # Create different types of accounts
    acc1 = CurrentAccount("John Doe", "001", 1000)
    acc2 = DepositAccount("Jane Smith", "002", 2000, 0.05, 3)
    acc3 = RestrictedAccount("Jim Brown", "003", 1500, 300)
    acc4 = AccountWithOverdraft("Jack Black", "004", 500, 200)

    # Add accounts to the bank
    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)
    bank.add_account(acc4)

    # Perform withdrawals
    print(bank.withdraw_from_account("001", 200))
    print(bank.withdraw_from_account("002", 500))
    print(bank.withdraw_from_account("003", 400))
    print(bank.withdraw_from_account("004", 600))

    # Perform deposits
    print(bank.deposit_to_account("001", 500))
    print(bank.deposit_to_account("002", 1000))

    # Save accounts to a file
    bank.save_accounts("accounts.txt")
