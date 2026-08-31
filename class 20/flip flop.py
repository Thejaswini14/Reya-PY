# Step 1: Define a function palind(r) that checks whether a tuple is a palindrome.

# Step 2: Set e to the tuple's last index, and s to its first index, 0.

# Step 3: Use a while loop that keeps comparing r[s] and r[e] as long as s is less than e.

# Step 4: Return False immediately the moment two compared items do not match.

# Step 5: Move s forward by one and e backward by one after every successful match.

# Step 6: Return True once the loop finishes without finding any mismatch.

# Step 7: Call palind(r) on r = (1, 2, 3, 3, 2, 1) and print whether it is Flip-Flop or not.




def palind(r):
    e = len(r)- 1
    f = 0 
    while f < e:
        if r[f] != r[e]:
            return False
        f += 1
        e -= 1
    return True
abcd = (1, 3, 5, 5, 3, 1)
if palind(abcd):
    print("it is a flip flop")
else:
    print("it is not a flip flop")
        
    