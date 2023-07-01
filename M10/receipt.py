import csv
from datetime import datetime 

PRODUCT_NUM_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
filename2 = 'request.csv'
key_column_index = 0
price = 0
name = ''
key = ''
row_list = {}
csv_dict = {}
products_dict = {}
request_dict = {}
receipt_key = ''
dates = datetime.now()
day = dates.weekday()

print('Inkom Emporium')
print()
def main():
    read_dictionary(filename, key_column_index)
    print('All Products')
    print(products_dict)
    

    with open(filename2, 'rt') as requests_file:
        checking = csv.reader(requests_file)
        #Skips first line
        next(checking)
        print()
        request_dict = {}
        for row_list in checking:
            requested_product = row_list[0]
            requested_quantity = float(row_list[1])
            request_dict[requested_product] = [requested_quantity]
        print('Requested Items')
    for request_dict in products_dict:
        value = products_dict[request_dict]
        name = value[0]
        price = float(value[1])
        print(f'{name}: {requested_quantity} @ {price}')
        if day == 1 or day == 2:
            discount = round(price * .10, 2)
            print(f'Discount: {discount:.2}')
            price -= discount
            subtotal = price * requested_quantity
            sales_tax = round(subtotal * .062)
            total = sales_tax + subtotal
            print(discount)
        else:
            subtotal = price * requested_quantity
            sales_tax = round(subtotal * .062)
            total = sales_tax + subtotal
    print()
    print(f'Sales tax: {sales_tax:.2f}')
    print(f'Total: {total:.2f}')
    print()
    print('Thank you for shopping at the Inkom Emporium.')
    current_date_and_time = datetime.now()
    print(f'{current_date_and_time:%A %I:%M %p}')
        
filename = 'products.csv'
def read_dictionary(filename, key_column_index):
    key_column_index = 0
    
    with open(filename, 'rt') as products_file:
        reader = csv.reader(products_file) 
        #Skips first line
        next(reader)
        for row_list in reader:
            product_number = row_list[0]
            name = row_list[1]
            price = row_list[2]
            products_dict[product_number] = [name, price]
        return products_dict
    
        
# Call main to start this program.
if __name__ == "__main__":
    main()