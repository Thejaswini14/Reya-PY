# Step 1: Define a class named pair_elements.

# Step 2: Inside the class, define a method twoSum(self, nums, target).

# Step 3: Inside the method, create an empty dictionary lookup to remember numbers you've already seen and their positions.

# Step 4: Loop through nums using enumerate(nums), so you get each position i and value num together.

# Step 5: On each pass, check whether target - num is already a key in lookup - if it is, return a tuple of that stored position and the current position i.

# Step 6: If not found yet, store the current number and its position in lookup using lookup[num] = i.

# Step 7: Take the target sum as input from the user, call twoSum() on the tuple (10, 20, 30, 40, 50, 60, 70), and print the two positions using an f-string.


class pair_elements:
    def twoSum(self, nums, target):
     dict = {} 
     for i,num in enumerate(nums):
            if target - num in dict:
                return (dict[target - num], i)
            dict[num] = i
qwaszx = int(input("Enter the target sum: "))
qqqq = pair_elements()
print("The two positions are: ", qqqq.twoSum((10, 20, 30, 40, 50, 60, 70), qwaszx))
