def swap_three_values(a, b, c):
    print(f"Mistaken positions: 1st = {a}, 2nd = {b}, 3rd = {c}")
    
    a, b, c = c, b, a
    
    print(f"Correct positions:  1st = {a}, 2nd = {b}, 3rd = {c}")
    return a, b, c

val1, val2, val3 = 30, 10, 20