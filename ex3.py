lines = input()
all_sold_quantity = 0
products = dict()
while lines != "Complete":
    commands = lines.split()
    command = commands[0]
    if command == "Receive":
        quantity = int(commands[1])
        product = commands[2]
        if quantity > 0:
            if product not in products.keys():
                products[product] = quantity
            else:
                products[product] += quantity
    elif command == "Sell":
        quantity = int(commands[1])
        product = commands[2]

        if product not in products.keys():
            print(f"You do not have any {product}.")
        else:
            last_quantity = products[product] - quantity
            if last_quantity < 0:
                print(f"There aren't enough {product}. You sold the last {products[product]} of them.")
                all_sold_quantity += products[product]
                del products[product]
            elif last_quantity == 0:
                products[product] -= quantity
                print(f"You sold {quantity} {product}.")
                all_sold_quantity += quantity
                del products[product]
            else:
                print(f"You sold {quantity} {product}.")
                products[product] -= quantity
                all_sold_quantity += quantity

    lines = input()
for food,quantity in products.items():
    print(f"{food}: {quantity}")

print(f"All sold: {all_sold_quantity} goods")