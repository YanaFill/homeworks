from new_bank import NewBankAccount
from bank import Money


class UpBankAccount(NewBankAccount):

    def __init__(self, account_number, owner_name, balance, currency, max_limit, max_count_transactions=5):
        super().__init__(account_number, owner_name, balance, currency, max_limit, max_count_transactions)
        self.balance = Money(balance, currency)

    def __eq__(self, other):
        if self.balance.currency == other.balance.currency:
            return True
        else:
            return False

    def __bool__(self):
        return self.balance.amount > 0

    def __add__(self, numb):
        self.deposit(numb)
        return id(self)

    def __sub__(self, numb):
        self.withdraw(numb)
        return id(self)

    def __call__(self, value=0):
        if value < 0:
            self.withdraw(value)
            print(f"It was written off from the balance {value} {self.balance.currency}")
        elif value > 0:
            self.deposit(value)
            print(f"The balance was replenished by the amount {value} {self.balance.currency}")
        elif value == 0:
            print(self.balance.amount)

    def __setattr__(self, name, value):
        if name == 'balance':
            old_balance = self.balance.amount if hasattr(self, 'balance') else 0
            self.__dict__["balance"] = Money(value, self.balance.currency if hasattr(self, 'balance') else 'USD')
            print(
                f"Change of balance: how much was {old_balance} {self.balance.currency} and became {self.balance.amount} {self.balance.currency}")
        else:
            super().__setattr__(name, value)


account1 = UpBankAccount(12345, "John Doe", 1000, "USD", 250)
account2 = UpBankAccount(54321, "Jane Smith", 500, "USD", 100)
print(f"Verification of the method __ eq__ : {account1 == account2}")
print()
# print(f"Verification of the method __bool__ для account1: {bool(account1)}")
# print(f"Verification of the method __bool__ для account2: {bool(account2)}")
# print()
# account1 + 500
# print(f"After application __add__: {account1.balance.amount}")
# account1 - 800
# print(f"After application __sub__: {account1.balance.amount}")
# print()
# account1(-300)
# account1(200)
print(f"After application __call__: {account1.balance.amount}")
print()
account1.balance = 2000









