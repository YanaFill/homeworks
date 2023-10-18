from bank import BankAccount


class NewBankAccount(BankAccount):
    def __init__(self, account_number: int, owner_name: str, balance: int, currency, max_limit, max_count_transactions=5):
        super().__init__(account_number, owner_name, balance, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.i = 0

        
    def transfer(self, recipient_account, amount):
        if amount < self.max_limit and self.i <= self.max_count_transactions:
            self.i += 1
            return super().transfer(recipient_account , amount)
        else:
            print("Перевищено кількість транзакцій або максимальний ліміт")

    def withdraw(self, amount):
        if amount < self.max_limit and self.i <= self.max_count_transactions:
            self.i += 1
            return super().withdraw(amount)
        else:
            print("Перевищено кількість транзакцій або максимальний ліміт")

    def add_percent(self, percentage=15):
        self.deposit(self.balance.amount * (percentage / 100))

if __name__ == '__main__':

    account1 = NewBankAccount(12345, "John Doe", 1000, "USD", 250)
    account2 = NewBankAccount(54321, "Jane Smith", 500, "USD", 100)

    print(account1)
    print(account2)
    account1.transfer(account2, 100)
    account1.withdraw(99)
    account1.add_percent()

    print()
    account2.transfer(account1, 19)
    account2.withdraw(12)
    account2.add_percent()

    print(account1)
    print(account2)
    