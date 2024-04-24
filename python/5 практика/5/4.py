import sqlite3
import hypothesis.strategies as st
from decimal import Decimal
from hypothesis import given
from fractions import Fraction

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        amount = float(amount)  # Преобразуем значение amount в тип float
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        return f"Баланс счета {self.account_number}: {balance}"

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"

account_numbers = st.integers(min_value=1000, max_value=9999).filter(lambda x: x not in existing_account_numbers)
existing_account_numbers = []
amounts = st.decimals(min_value=0, max_value=100000)

@given(account_numbers, amounts)
def test_deposit(account_number, amount):
    account = BankAccount(account_number)
    account.create_account(0)
    before_balance = float(account.check_balance().split(": ")[1])
    amount = float(amount)  # Преобразуем значение amount в тип float
    account.deposit(amount)
    after_balance = float(account.check_balance().split(": ")[1])
    assert after_balance == before_balance + amount

if __name__ == "__main__":
    test_deposit()
