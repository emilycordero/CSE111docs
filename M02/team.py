'''
Emily Cordero
Brother Eisinger
discount.py 
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets the current day of the week from your computer’s operating system.
'''
# importing a library on time
from datetime import datetime

dates = datetime.now()
day = dates.weekday()
price = 1
total = 0
discount = 0

price = float(input('Please enter the price of item: '))
while price != 0:
    if price != 0:
        quantity = int(input('How many will you get? '))
        subtotal = price * quantity
        print()
    if subtotal >= 50 and (day == 1 or day == 2):
        discount = round(subtotal * .10, 2)
        print(f'Discount: {discount:.2}')
        subtotal -= discount
    elif subtotal <= 50 and (day == 1 or day == 2):
        difference = subtotal - 50
        print(f'${difference} is left to get a 10% discount! You currently have: {subtotal}.')
        
    sales_tax = round(subtotal * .06,2)
    total = sales_tax + subtotal
    print(f'Sales tax: {sales_tax:.2}')
    print(f'Total: {total:.2f}')
    price = float(input('Please enter the subtotal: '))