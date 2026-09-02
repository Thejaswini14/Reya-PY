# Step 1: Create two fruit baskets as sets, each holding some repeated fruit names.

# Step 2: Add a new fruit into the first basket using add().

# Step 3: Find the fruits shared between both baskets using intersection().

# Step 4: Create an array of fruit counts using the array module.

# Step 5: Add new fruit counts into the array using insert() and append().

# Step 6: Count how many times a chosen number appears in the array.

# Step 7: Reverse the order of the fruit counts array and print the final organizer summary.


basket1 = {"apple", "guava", "blueberrys", "bananas", "strawberry"}
basket2 = {"apple", "orange", "rasberrys", "grapes"}
basket1 = {"apple", "guava", "blueberrys", "bananas", "strawberry"}
basket1.add("mango")
print(basket1)
common = basket1.intersection(basket2)
print(common)
import array as arr
a = arr.array('i', [5, 4])
print(a)
a.insert(1, 3)
a.append(2)
print(a)
(a.reverse())
print(a.count(5))
print(a)