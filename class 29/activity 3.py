# Step 1: Define a class India with three methods: capital(), language(), and type(), each printing a fact about India.

# Step 2: Define a class USA with the exact same three method names, each printing a fact about the USA.

# Step 3: Create one object of each class: obj_ind and obj_usa.

# Step 4: Use a for loop to iterate through (obj_ind, obj_usa).

# Step 5: Inside the loop, call country.capital(), country.language(), and country.type() on each object - Python automatically runs each class's own version, with no inheritance needed.


class India:
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language in India.")
    def type(self):
        print("India is a federal parliamentary democratic republic.")
class USA:
    def capital(self):
        print("Washington, D.C. is the capital of the USA.")
    def language(self):
        print("English is the most widely spoken language in the USA.")
    def type(self):
        print("The USA is a federal presidential constitutional republic.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    