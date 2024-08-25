import os
from grocery import read_grocery_file

def main():
    print ("reading grocery list")

    grocery_file = os.path.join(os.path.dirname(__file__), "resources", "grocery_list.csv")
    grocery_list = read_grocery_file(grocery_file)
    
    for item in grocery_list:
        print ("{:<20} {:>10.2f} {:<10}".format(item.name, item.price, item.type.name))

if __name__ == "__main__":
    main()    

