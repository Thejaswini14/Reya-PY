# Step 1: Start a try block.

# Step 2: Ask the user for a first number and a second number, converting each with int(input(...)).

# Step 3: Divide the first number by the second and print the result.

# Step 4: Add an except ZeroDivisionError block, printing "Division by zero is error !!" if the second number is 0.

# Step 5: Add an except ValueError block, printing a message asking for valid whole numbers if either entry isn't a number.

# Step 6: Add a plain except block, printing "Wrong input" for any other unexpected error.

# Step 7: Add an else block that prints "No exceptions" only if the division succeeded with no errors at all.

# Step 8: Add a finally block that prints "This will execute no matter what", always running regardless of the outcome. 


try:
    user1 = int(input("enter a number"))
    user2 = int(input("enter another number"))
    number = user1 / user2
    print("result", number)
except ZeroDivisionError as ex:
    print("Division by zero is error !!", ex)
except ValueError as qwerty:
    print("wrong input", qwerty)
else:
    print("no accexceptions")
finally:
    print("This will execute no matter what")