# Step 1: Import ABC and abstractmethod from Python's abc module.

# Step 2: Define an abstract base class Absclass that inherits from ABC.

# Step 3: Inside Absclass, define a normal method print(self, x) that prints the passed-in value.

# Step 4: Define an abstract method task(self) using the @abstractmethod decorator.

# Step 5: Define a subclass test_class that inherits from Absclass and implements task(self), printing its own message.

# Step 6: Create an object test_obj of test_class - this works because task() has been properly implemented.

# Step 7: Call test_obj.task() to run the overridden method, then call test_obj.print(100) to run the inherited normal method.



from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self, x):
        print(x)
    @abstractmethod
    def task (self):
        print("we are inside the abstract class")
class test_class(AbstractClass):
    def task(self):
        print("this is a sub class")
obj1 = test_class()
obj1.task()
obj1.print(100)
