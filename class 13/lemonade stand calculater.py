def greet_custumer():
    print("Welcome to the Lemonade Stand!")
    print("We sell lemonade for $3.00 per cup.")
    print("How many cups would you like to buy?")
greet_custumer()
def calculate_total(price, cups):
    total = price * cups
    return total

user_input = input("Enter the number of cups you want to buy: ")
price = int(input("Enter the price of lemonade per cup: "))
print("total price is:")
print(calculate_total(price, int(user_input)))
total = calculate_total(price, int(user_input))
def calculate_change(total, customer_paid):
    change = customer_paid - total
    return change
customer_paid = int(input("Enter the amount paid by the customer: "))
print("the total returned change to customer is:")
print(calculate_change(total, customer_paid))


