'''
Emily Cordero
Brother Eisinger
tire_volume.py 
Write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.
'''
import math
width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the tire in inches (ex 15): '))

v = ((math.pi * width ** 2) * ratio)*((width * ratio) + (2540*diameter)) / 10000000000

print(f'The approximate volume is {v:.2f} liters')