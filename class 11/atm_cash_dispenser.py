# Step 1: Set up six counter variables (one per note value) plus counters for customers served and total dispensed, all starting at 0.

# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving becomes False.

# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a message and continue back to the top of the loop.

# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values one at a time and works out how many of each note to dispense.

# Step 5: Update the matching counter variable for whichever note value was just dispensed, then ask if there is a next customer, setting serving to False if not.

# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six note values to print the daily denomination report.

# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that value dispensed across the whole day.


note_1000 = 0   
note_500 = 0
note_200 = 0
note_100 = 0
note_50 = 0
note_20 = 0
customers_served = 0
total_dispensed = 0
serving = True
while serving:
    customer_name = input("Enter customer name: ")
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    if withdrawal_amount <= 0 or withdrawal_amount % 10 != 0:
        print("Invalid amount. Please enter a positive amount that is a multiple of 10.")
        continue
    print(f"dispensing amount: {withdrawal_amount}for {customer_name}")
    remaining_amount = withdrawal_amount
    id = 1 
    while id <= 6: 
        if id == 1:
            note_value = 1000
        elif id == 2:
            note_value = 500
        elif id == 3:
            note_value = 200
        elif id == 4:
            note_value = 100
        elif id == 5:
            note_value = 50
        else:
            note_value = 20
        num_notes = remaining_amount // note_value
        if num_notes > 0:
            print(f"number notes of {num_notes} of {note_value}")
            remaining_amount -= num_notes * note_value
            if id == 1:
                note_1000 += num_notes
            elif id == 2:
                note_500 += num_notes
            elif id == 3:
                note_200 += num_notes
            elif id == 4:
                note_100 += num_notes
            elif id == 5:       
                note_50 += num_notes
            else:
                note_20 += num_notes
        id += 1 
    print(f"remaining amount: {remaining_amount}")
    next_customer = input("Is there a next customer? (yes/no): ")
    if next_customer == "no":
      serving = False
             
    customers_served += 1
    total_dispensed += withdrawal_amount
    print(f"total customers served: {customers_served}")
    print(f"total amount dispensed: {total_dispensed}")
for i in range(1, 7):
    if i == 1:
        note_value = 1000
        num_notes = note_1000
    elif i == 2:
        note_value = 500
        num_notes = note_500
    elif i == 3:
        note_value = 200
        num_notes = note_200
    elif i == 4:
        note_value = 100
        num_notes = note_100
    elif i == 5:
        note_value = 50
        num_notes = note_50
    else:
        note_value = 20
        num_notes = note_20
    print(f"notes of {note_value}: {num_notes} ", end="")
    for j in range(num_notes):
        print("*", end="")
    print()