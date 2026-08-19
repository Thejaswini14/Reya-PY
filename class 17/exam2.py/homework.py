months =  ("January", "February", "March", "April", 
    "May", "June", "July", "August", 
    "September", "October", "November", "December")
try:
    num = int(input("Enter a month number (1-12): "))
    if 1 <= num <= 12:
        print(f"The month is: {months[num - 1]}")
    else:
        print("Invalid number! Please enter a number between 1 and 12.")
except ValueError:
    print("Please enter a valid integer.")
