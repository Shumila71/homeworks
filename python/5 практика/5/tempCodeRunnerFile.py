    # Преобразуем значение amount в тип float
        amount = float(amount)
        # Используем кортеж с одним элементом для передачи параметра в execute
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        ret