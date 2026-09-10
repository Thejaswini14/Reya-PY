# Step 1: Define a class named IOString.

# Step 2: Inside the class, define __init__(self) as the constructor, setting self.str1 to an empty string.

# Step 3: Define a method get_String(self) that asks the user to enter a string and stores it in self.str1.

# Step 4: Define a method print_String(self) that converts self.str1 to uppercase using .upper() and prints the result.

# Step 5: Create an object of the IOString class and store it in str1.

# Step 6: Call str1.get_String() to read the user's input.

# Step 7: Call str1.print_String() to print the uppercase string.



class IOString:
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("Enter a string: ")
    def print_String(self):
        print(self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()
