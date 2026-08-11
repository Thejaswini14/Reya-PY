# Step 1: Define a function total_calc(bill_amount, tip_perc) with two positional parameters.

# Step 2: Calculate the total by adding the tip percentage onto the bill amount.

# Step 3: Round the total to two decimal places using round().

# Step 4: Print the final total using an f-string.

# Step 5: Call total_calc(150, 20), passing the bill amount and tip percentage in that exact order.

# ------------------------------------------------------------

# Activity 2: Cube of the Cube

 

# WHAT YOU WILL BUILD

# You define one function to cube a number, then define a second function that calls the first only when the number divides evenly by 3.

def total_calc (bill_amount, tipperc):
  total_calc = (tipperc * bill_amount) / 100
  return total_calc + bill_amount
print(total_calc(200, 30))
