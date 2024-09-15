#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        for _ in range(quantity):
          self.items.append(title)
        self.transactions.append((price, quantity))

    def apply_discount(self):
        if self.discount == 0:
            print('There is no discount to apply.')
        else:
            self.total = self.total * (100 - self.discount) / 100
            print(f'After the discount, the total comes to ${int(800)}.')

    def void_last_transaction(self):
        last_trx = self.transactions.pop()
        self.total -= (last_trx[0] * last_trx[1])
        for _ in range(last_trx[1]):
            self.items.pop()