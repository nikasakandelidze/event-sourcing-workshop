
class Account():
    def __init__(self, id: str, owner: str) -> None:
        self.balance = 0
        self.id = id
        self.owner = owner

    def deposit_money(self, money: int):
        self.balance += money

    def withdraw_money(self, money: int):
        if money < self.balance:
            self.balance -= money
