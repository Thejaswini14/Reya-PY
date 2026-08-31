# Step 1: Create a tuple called tuplex holding four different data types together.

# Step 2: Create a new tuple called tuplex holding six integers.

# Step 3: Use the + operator to add a single new item, 9, onto tuplex, since tuples cannot be changed directly.

# Step 4: Create tuple1 and use .count(50) to count how many times 50 appears inside it.

# Step 5: Create a longer tuple called tuplex to practice slicing.

# Step 6: Slice tuplex[3:5] to get a range starting from index 3.

# Step 7: Slice tuplex[:6] to get every item from the very beginning through index 5



tuplex = ("string", "integer", "float", "boolean")
tuplex = (1, 5, 4, 2, 3, 6)
tuplex = tuplex + (9,)
print(tuplex)
tuple1 = (1, 5, 4, 2, 3)
print(tuple1.count(5))
tuplex = (1, 4, 3, 6, 2, 5, 7)
slice = tuplex[1:5]
print(slice)
slice = tuplex[:6]
print(slice)