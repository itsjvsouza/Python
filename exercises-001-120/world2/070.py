over_1000 = 0
total = 0
chepest_product_price = 0

while True:
    product_name = input("\nEnter the name of the product: ")
    product_price = float(input("Enter the price of the product: "))

    total += product_price

    if chepest_product_price == 0:
        chepest_product = product_name
    else:
        if product_price < chepest_product_price:
            chepest_product = product_name

    if product_price > 1000:
        over_1000 += 1

    choise = input("\nDo you want to continue? (Y/N): ").lower()

    if choise == "n":
        break

print(f"\nQuantity of products over $1000: {over_1000}")
print(f"Total spent: ${total}")
print(f"Cheapest product: {chepest_product}")
