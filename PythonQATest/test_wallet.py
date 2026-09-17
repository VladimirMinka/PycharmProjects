import pytest
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return Wallet(100)


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

@pytest.fixture
def wallet():
    return Wallet(100)

def test_initial_balance(wallet):
    assert wallet.balance == 100

def test_withdraw(wallet):
        wallet.withdraw(30)
        assert wallet.balance == 70
