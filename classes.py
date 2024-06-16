class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses")

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful! New balance: {self.balance}"

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class CurrentAccount(Account):
    def __init__(self, name, account_number, balance, cheques_issued=0):
        super().__init__(name, account_number, balance)
        self.cheques_issued = cheques_issued

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds for withdrawal."
        self.balance -= amount
        self.cheques_issued += 1
        return f"Withdrawal successful! Remaining balance: {self.balance}, Cheques issued: {self.cheques_issued}"


class DepositAccount(Account):
    def __init__(self, name, account_number, balance, interest_rate, withdrawals_limit):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate
        self.withdrawals_limit = withdrawals_limit
        self.withdrawals_count = 0

    def withdraw(self, amount):
        if self.withdrawals_count >= self.withdrawals_limit:
            return "Withdrawal limit reached."
        if amount > self.balance:
            return "Insufficient funds for withdrawal."
        self.balance -= amount
        self.withdrawals_count += 1
        return f"Withdrawal successful! Remaining balance: {self.balance}"

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return f"Interest applied! New balance: {self.balance}"


class RestrictedAccount(CurrentAccount):
    def __init__(self, name, account_number, balance, max_withdrawal_limit):
        super().__init__(name, account_number, balance)
        self.max_withdrawal_limit = max_withdrawal_limit

    def withdraw(self, amount):
        if amount > self.max_withdrawal_limit:
            return f"Cannot withdraw more than the limit of {self.max_withdrawal_limit}."
        return super().withdraw(amount)


class AccountWithOverdraft(CurrentAccount):
    def __init__(self, name, account_number, balance, overdraft_limit):
        super().__init__(name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Overdraft limit exceeded."
        self.balance -= amount
        return f"Withdrawal successful! Remaining balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def withdraw_from_account(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        return "Account not found."

    def deposit_to_account(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.deposit(amount)
        return "Account not found."

    def apply_interest_to_deposit_accounts(self):
        for account in self.accounts:
            if isinstance(account, DepositAccount):
                print(account.apply_interest())

    def save_accounts(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"{account}\n")

    def load_accounts(self, filename):
        # This would typically involve reading from a file and reconstructing account objects
        pass  # Implement this method as needed for your system
