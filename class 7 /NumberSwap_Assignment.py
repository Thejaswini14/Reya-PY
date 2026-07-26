# Initial values
a = 10
b = 20
c = 30

print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Python first evaluates the right side:
# (b, a, c) -> (20, 10, 30)
# Then assigns:
# a = 20
# b = 10
# c = 30

a, b, c = c, a, b
#a, c,b= c, a, b
print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)