# Step 1: Define a class named myClass.

# Step 2: Inside the class, create a private class variable __privateVar set to 27.

# Step 3: Define a private method __privMeth(self) that prints a short message.

# Step 4: Define a public method hello(self) that prints __privateVar's value using myClass.__privateVar.

# Step 5: Create an object foo of the myClass class.

# Step 6: Call foo.hello() - since hello() is a method inside the class, it reaches the private variable with no trouble.

# Step 7: Try reaching foo.__privMeth from outside the class - Python raises an AttributeError, proving a private method really can't be reached this way from outside.


class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("This is a private method.")
    def hello(self):
        print("Private variable value is:", myClass.__privateVar )
obj = myClass()
obj.hello()
obj.__privMeth()
