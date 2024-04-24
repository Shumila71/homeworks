class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма для зачисления не может быть отрицательной.")
        self._balance += amount
        return f"{amount} средств успешно зачислены на счет {self._account_number}"

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма для снятия не может быть отрицательной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")
        self._balance -= amount
        return f"{amount} средств успешно сняты с счета {self._account_number}"

    def check_balance(self):
        return f"Баланс счета {self._account_number}: {self._balance}"
    
try:
    account = BankAccount("12345", -100)
except ValueError as e:
    print(e)

account = BankAccount("12345", 100)
try:
    account.withdraw(-200)
except ValueError as e:
    print(e)