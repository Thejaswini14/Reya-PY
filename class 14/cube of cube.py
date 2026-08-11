# Step 1: Define a function cube(number) that returns the number multiplied by itself three times.

# Step 2: Define a function by_three(number) that checks if the number is divisible by 3.

# Step 3: If it is divisible by 3, call and return cube(number) from inside by_three().

# Step 4: If it is not divisible by 3, return False instead.

# Step 5: Call by_three(9) and by_three(4), and print both results.


def cuboid (number):
   return number * number * number
def by_three(number):
   if number % 3 == 0:
     return cuboid (number)
   else:
      return "number not divisible by three"
print(by_three(6))
   
   
    