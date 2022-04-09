def get_invoice_items(items):
    # Write your code here
    invoice_items = []

    for item in items:
        total_price = float(item['quantity']) * float(item['price'])
        formated_price = format(total_price, '.3f')
        item_name = str(item['name']).capitalize()
        total_items = str(item['quantity'])
        invoice_items += [f'{total_items} {item_name} {formated_price}KD']

    
    return invoice_items



def get_total(items):
    # Write your code here
    total = 0

    for item in items:
        item_price = float(item['quantity']) * float(item['price'])
        total += item_price

    return total



def print_receipt(invoice_items, total):
    # Write your code here
    string_total = format(total, '.3f')
    print("-" * 19)
    print("receipt")
    print("-" * 19)
    for item in invoice_items:
        print(item)
    print("-" * 19)
    print('\n')
    print(f'Total Price: {string_total}KD')
    
def main():
    items = []

    user_is_entering_products = True

    
    while(user_is_entering_products):
        item_name = input("Enter item name (enter \'done\' when finished): ")
        if item_name == 'done':
            user_is_entering_products = False
            break
        item_quantity = input("Enter quantity: ")
        item_price = input("Enter price: ")
        product = {'name':item_name, "quantity":item_quantity, "price": item_price }
        items += [product]

    # if i remove this print statement the test fails even though the solution works
    print(items)
            
    # Write your main logic here
    invoice_items = get_invoice_items(items)
    total = get_total(items)

    print_receipt(invoice_items, total)


if __name__ == "__main__":
    main()
