import csv

from grocery import GroceryType, GroceryItem

def read_grocery_file(filename):
    grocery_list = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, price, grocery_type = row
            price = float(price)  # convert price to float
            grocery_type = GroceryType[grocery_type]
            grocery_item = GroceryItem(name, price, grocery_type)
            
            grocery_list.append(grocery_item)

    print(f"Read {len(grocery_list)} items from {filename}")

    return grocery_list

