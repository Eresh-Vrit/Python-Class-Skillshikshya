# Shopping Cart using Accumulators and a List

total = 0
item_count = 0
cart = []   # Stores item names

while True:
    item = input("Enter item name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input(f"Enter price of {item}: $"))

    cart.append(item)      # Add item to the cart
    total += price         # Accumulate total price
    item_count += 1        # Accumulate number of items

    print(f"\n{item} added to cart!")
    print(f"Items in Cart: {item_count}")
    print(f"Current Total: ${total:.2f}")
    print(f"Cart: {cart}\n")

print("\n====== Shopping Summary ======")
print(f"Items Purchased: {cart}")
print(f"Total Items: {item_count}")
print(f"Final Total: ${total:.2f}")