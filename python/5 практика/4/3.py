from typing import Protocol

class BankAccount(Protocol):
    def balance(self) -> float:
        ...

def deal(account: BankAccount, amount: float, max_limit: float) -> None:
    new_balance = account.balance() + amount
    if new_balance > max_limit:
        raise ValueError("Превышен максимальный лимит")

class BankAccountImpl:
    def __init__(self, account_number: str, balance: float = 0):
        self._account_number = account_number
        self._balance = balance

    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> str:
        if amount < 0:
            raise ValueError("Сумма для зачисления не может быть отрицательной.")
        self._balance += amount
        return f"{amount} средств успешно зачислены на счет {self._account_number}"

    def withdraw(self, amount: float) -> str:
        if amount < 0:
            raise ValueError("Сумма для снятия не может быть отрицательной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")
        self._balance -= amount
        return f"{amount} средств успешно сняты с счета {self._account_number}"

    def check_balance(self) -> str:
        return f"Баланс счета {self._account_number}: {self._balance}"


def main():
    account = BankAccountImpl("12345", 100)
    try:
        deal(account, 200, 300)  # Превышен максимальный лимит
    except ValueError as e:
        print(e)

    try:
        deal(account, -50, 300)  # Сумма для зачисления не может быть отрицательной.
    except ValueError as e:
        print(e)

    try:
        deal(account, 50, 100)  # Превышен максимальный лимит
    except ValueError as e:
        print(e)