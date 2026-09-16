# Step 1: Create a parent class called FamilyMember that stores shared traits like eye colour and height.

# Step 2: Create a child class called Kid that inherits from FamilyMember.

# Step 3: Give Kid its own details, then use super().__init__() to pull in the parent's traits too.

# Step 4: Override show_traits() inside Kid to display the kid's own details plus the inherited ones.

# Step 5: Add a brand new method inside Kid that only the child class has.

# Step 6: Create a Kid object and call both the overridden method and the new method.

# Step 7: Check with issubclass() whether Kid truly is a subclass of FamilyMember.


class FamilyMember:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height
        print(self.eye_color, self.height)
class Kid(FamilyMember):
    def __init__(self, eye_color, height, age, name):
        super().__init__(eye_color, height)
        self.age = age
        self.name = name
    def show_traits(self):
        print(self.eye_color, self.height, self.age, self.name)
    
    def Hobby(self, hobby):
        print(self.name + " likes " + hobby)
kid1 = Kid("brown", "5'5", 11, "reya")
kid1.Hobby("painting")
kid1.show_traits()
print(issubclass(Kid, FamilyMember))
kid2 = Kid("brown", "3'4", 5, "devitha")
kid2.Hobby("playing")
kid2.show_traits()
print(issubclass(Kid, FamilyMember))
