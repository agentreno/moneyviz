# coding: utf-8
import random
transactions = []
transaction_line = '{:02d}/01/15,"ABC",-{:.2f},{:.2f}'
starting_balance = 500
transaction_count = 80
for i in range(transaction_count):
    transaction_amt = random.randint(1,2000) / 100.0
    day = 1
    starting_balance -= transaction_amt
    transactions.append(transaction_line.format(day, transaction_amt, starting_balance))
transactions.reverse()

print("Date,Description,Amount,Balance")
for line in transactions:
   print(line)
