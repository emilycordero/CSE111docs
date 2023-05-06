'''
Emily Cordero
heart_rate.py
Write a python program that gets input from user, uses a variable and performs arithmetic and displays results for user to see. 

'''
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input('Please enter your age: '))

max_heart_rate = 220 - age

slowest_heart_rate = float(max_heart_rate) * .65
fastest_heart_rate = float(max_heart_rate) * .85

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {slowest_heart_rate:.0f} and {fastest_heart_rate:.0f} beats per minute.')

