# Step 1: Start a try block.

# Step 2: Inside it, ask the user to enter a number and convert it to an integer using int(input(...)).

# Step 3: Print the number that was entered.

# Step 4: Add an except ValueError as ex block to catch invalid, non-numeric input.

# Step 5: Inside the except block, print "Exception:" followed by the caught exception object, ex, showing Python's own error message.

try: 
    user = int(input("enter a number"))
    print("number", user)
except ValueError as ex:
    print("exeption", ex)
    
