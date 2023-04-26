from luhn_validator import validate


class User:
    def __init__(self, user, card, limit):
        self.user = user
        self.card = card
        self.limit = limit
        self.balance = 0 if validate(card) else "error"
        self.transaction_is_invalid = (
            lambda amount, action: self.balance == "error" or (self.balance + amount > self.limit and action == 'charge')
        )

    def charge(self, amount):
        if self.transaction_is_invalid(amount, 'charge'):
            return
        self.balance += amount

    def credit(self, amount):
        if self.transaction_is_invalid(amount, 'credit'):
            return
        self.balance -= amount
