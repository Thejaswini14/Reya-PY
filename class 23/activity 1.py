# Step 1: Create a list of store item names and a list of matching stock counts.

# Step 2: Pair items with stock counts into a dictionary using zip() and dictionary comprehension.

# Step 3: Filter out only the items that are still in stock using list comprehension.

# Step 4: Ask which item the shopper wants to buy.

# Step 5: Stop the checker immediately using exit() if that item has run out.

# Step 6: Apply a markup to every price using map().

# Step 7: Print the final price paid and the updated inventory.



store_items = ["pencils", "eraser", "pen", "correction tape", "notebooks", "highlighters"]
stock_counts = [20, 11, 9, 8, 15, 7]
inventory = {item: count for item, count in zip (store_items, stock_counts)}
print(inventory)
in_stock = [item for item in store_items if inventory [item]> 0]
print(in_stock)
purchase = str(input("which item would you like to buy?"))
if purchase not in inventory:
    print("sorry we do not have the item you were looking for ")
    exit()
prices = [10, 15, 20, 50, 100, 30]
price = int(input("what is the up price"))
new_price = list(map(lambda abc: abc + price, prices ))
print(new_price)
inventory[purchase] = inventory[purchase] -1
print(inventory[purchase])


