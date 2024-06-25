#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    for i in range(quantity):
      self.items.append(title)
    self.transactions.append({'price': price, 'quantity': quantity})

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total *= ((100 - self.discount) / 100)
      print(f'After the discount, the total comes to ${int(self.total)}.')

  def void_last_transaction(self):
    last_transaction = self.transactions[len(self.transactions) - 1]
    self.total -= (last_transaction['price'] * last_transaction['quantity'])
    self.transactions = self.transactions[:len(self.transactions) - 1] 



cash_register = CashRegister(20)
cash_register.add_item('burgers', 10, 3)
cash_register.add_item('dogs', 5, 3)
print(cash_register.total)
print(cash_register.transactions)
cash_register.void_last_transaction()
print(cash_register.total)
print(cash_register.transactions)