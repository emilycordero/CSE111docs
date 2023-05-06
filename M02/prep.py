#Python includes many built-in functions such as: input, int, float, str, len, range, abs, round, list, dict, open, and print. 
import math
name = input('Enter your name: ')
print(f'Hello {name}')

n = float(input('Please enter number: '))
r = round(n,2) # Without ndigits it will be rounded to nearest integer
print(r)

x = 'sun'
y = 'moon'
z = 'stars'
print(x,y,z, sep='|', flush = False)

r = math.sqrt(85)
print(r)