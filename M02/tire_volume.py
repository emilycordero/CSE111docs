'''
Emily Cordero
Brother Eisinger
tire_volume.py 
Write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.
'''
import math
from datetime import datetime, date

price = 0
current_date = datetime.now().date()

width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the tire in inches (ex 15): '))

v = ((math.pi * width ** 2) * ratio)*((width * ratio) + (2540*diameter)) / 10000000000

print(f'The approximate volume is {v:.2f} liters')

if width >= 12 and width <= 15:
    price = 80
elif width >= 16 and width <= 20:
    price = 100
elif width >= 21 and width <= 26:
    price = 200
else:
    price = int(input('Enter price: '))
print(price)

user_response = input('Do you want to buy a tire with the dimension entered? ')

with open("volumes.txt", mode="at") as volumes_file:
    if user_response == 'yes':
        phone_number = input('Please enter phone number: ')
    print(f"{current_date}, {width}, {ratio}, {diameter}, {v:.2f}, {price}, {phone_number}", file=volumes_file)
    