from bank import BankAccount
import pytest

@pytest.fixture
def create_obj():
    return BankAccount(12345, "John Doe", 1000, "EUR")


def test_deposit(create_obj):
    create_obj.deposit(100)
    assert create_obj.balance.amount == 1100


def test_withdraw(create_obj):
    create_obj.withdraw(99)
    assert create_obj.balance.amount == 901


def test_change_owner_name(create_obj):
    create_obj.change_owner_name("Mike")
    assert create_obj.owner_name == "Mike"


def test_transfer(create_obj):
    account2 = BankAccount(54321, "Jane Smith", 500, "USD")
    create_obj.transfer(account2,250)
    assert create_obj.balance.amount == 750
    assert account2.balance.amount == 750


def test_check_account_number(create_obj):
    assert create_obj.check_account_number(create_obj.account_number) is True


