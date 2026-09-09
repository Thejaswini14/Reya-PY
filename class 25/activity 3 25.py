# Step 1: Define a class named Parrot.

# Step 2: Inside the class, create a class variable species set to "bird".

# Step 3: Define __init__(self, name, age), storing both values onto self.name and self.age.

# Step 4: Create two objects, blu and woo, passing in each parrot's own name and age.

# Step 5: Print each object's shared species value, then print each object's own name and age.



class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print("blu", blu.species, blu.name, blu.age)    
print("woo", woo.species, woo.name, woo.age)
