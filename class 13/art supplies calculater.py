def greet_customer():
    print("welcome to the art supplies store!") 
    print("get your colors, brushes and paints here!")
greet_customer()

price_per_item = float(input("Enter the price per art item in dollars: "))
items_bought =float(input("Enter the number of art items bought: "))
def calculate_total(price, items):
    total = price * items
    return total
total_cost = calculate_total(price_per_item, items_bought)

rounded_total = round(total_cost, 2)
print("total cost:" , rounded_total)

amount_paid = float(input("Enter the amount paid by the customer in dollars: "))
def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message():
    if items_bought >= 5:
        return "great choice! you picked many art supplies for your creative projects. "
    else:
        return "thanks for shopping at the art supplies store!"

closing_message = thank_you_message(items_bought)




