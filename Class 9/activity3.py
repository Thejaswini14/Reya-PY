# 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.

# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).

number =int(input("a number that is greater than 1"))
print("the reverse of the number")
for i in range(number,0, -1):
    print(i)
