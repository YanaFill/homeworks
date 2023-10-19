class Money:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def str(self):
        return f"{self.amount} {self.currency}"
class BankAccount:
    accounts = []

    def __init__(self, account_number: int, owner_name: str, balance: int, currency):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = Money(balance, currency)
        self.accounts.append(self)

    def __str__(self):
        return f"Рахунок #{self.account_number}, Баланс: ${self.balance.amount:.2f}, Власник: {self.owner_name}"

    def deposit(self, amount):
        if amount > 0:
            self.balance.amount += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance.amount >= amount:
            self.balance.amount -= amount
            return True
        else:
            return False

    def change_owner_name(self, new_owner_name):
        self.owner_name = new_owner_name

    def display_account_info(self):
        print(self)

    def transfer(self, recipient_account, amount):
        if amount > 0 and self.balance.amount >= amount:
            if recipient_account.deposit(amount):
                self.balance.amount -= amount
                return True
        return False

    @staticmethod
    def check_account_number(account_number):
        return len(str(account_number)) == 5

    @property
    def print_account_number(self):
        return self.account_number

    @print_account_number.setter
    def print_account_number(self, new_account_number):
        if BankAccount.check_account_number(new_account_number):
            self.account_number = new_account_number
        else:
            print("Помилка: Некоректний номер рахунку")

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total_balance = sum(account.balance.amount for account in cls.accounts)
        return total_balance / len(cls.accounts)

if __name__ == '__main__':

    account1 = BankAccount(12345, 1000.0, "John Doe", "EUR")
    account2 = BankAccount(54321, 500.0, "Jane Smith", "USD")

    account1.display_account_info()
    account2.display_account_info()
    print()
    account1.deposit(200.0)
    account2.withdraw(100.0)

    account1.display_account_info()
    account2.display_account_info()
    print()
    account1.change_owner_name("John Smith")
    account2.change_owner_name("Jane Doe")

    account1.transfer(account2, 300.0)

    account1.display_account_info()
    account2.display_account_info()
    print()
    print("Валідність номеру рахунку:", BankAccount.check_account_number(account1.account_number))

    account1.account_number = 54321

    account1.display_account_info()

