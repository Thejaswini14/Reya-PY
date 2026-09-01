# Step 1: Create test_dict, a dictionary of five words, each holding a number value.

# Step 2: Print the original dictionary before counting anything.

# Step 3: Store the target value K that you want to search for.

# Step 4: Set a counter, res, to zero before the loop begins.

# Step 5: Loop through every key in test_dict and compare its value to K.

# Step 6: Add one to res every time a value matches K.

# Step 7: Print the final frequency count once the loop finishes.



test_dict = {"one": "21", "two": "22", "three": "21", "four": "25", "six": "26"}
print(test_dict)
k = "26"
counter = 0
for i in test_dict:
    if test_dict[i]== k:
        counter += 1
print(counter)
