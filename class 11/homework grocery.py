low_price = 0
medium_price = 0 
high_price = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input(f"Hello {customer_name}, how many items are you buying? "))
    total_amount = 0

    for i in range(item_count):
        item_price = float(input(f"Enter price for item {i + 1}: "))
        total_amount += item_price

        if item_price < 10:
            low_price += 1
        elif 10 <= item_price < 50:
            medium_price += 1
        else:
            high_price += 1

    print(f"Total amount for {customer_name}: ${total_amount:.2f}")
    total_sales += total_amount
    customers_served += 1

   


    print(f"Total customers served: {customers_served}")
    print(f"Total sales amount: ${total_sales:.2f}")
    print(f"Items under 10 rs: {low_price}")
    print(f"Items between 10 rs and 50 rs: {medium_price}")
    print(f"Items over 50 rs: {high_price}")


    print("Thank you for shopping with us!\n") 
