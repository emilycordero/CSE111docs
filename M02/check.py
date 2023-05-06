'''
Emily Cordero
Brother Eisinger
CSE 111
Write a Python program named boxes.py that asks the user for two integers:
the number of manufactured items
the number of items that the user will pack per box
'''
import math
number_of_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

total_boxes = math.ceil(number_of_items / items_per_box)

print(f'For {number_of_items}, packing {items_per_box} in each box, you will need {total_boxes} boxes.')

