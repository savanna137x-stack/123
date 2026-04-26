class Bank:
    def __init__(self):
        self.account = None
    def open_account(self):
        self.account = 0
        print("cчет открыт баланс: 0")
    def close_account(self):
        self.account = None
        print("счет закрыт")

    def deposit(self, amount):
        if self.account is not None:
            self.account += amount
            print(f"пополнено: {amount} текущий баланс: {self.account}")
        else:
            print("ошибка: сначала откройте счет")

    def withdraw(self, amount):
        if self.account is not None:
            if self.account >= amount:
                self.account -= amount
                print(f"снято: {amount} Остаток: {self.account}")
            else:
                print("недостаточно средств на счете")
        else:
            print("ошибка: нельзя снять деньги с закрытого счета")

b = Bank()
b.open_account()
b.deposit(1000000000)
b.withdraw(40000)
b.close_account()
