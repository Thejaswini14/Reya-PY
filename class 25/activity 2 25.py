# Step 1: Define a class named Vehicle.

# Step 2: Inside the class, define __init__(self, max_speed, mileage) as the constructor method.

# Step 3: Inside __init__, store both passed-in values onto self.max_speed and self.mileage.

# Step 4: Create an object named modelX by calling Vehicle(240, 18).

# Step 5: Print modelX.max_speed and modelX.mileage using the object.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print(modelX.max_speed)
print(modelX.mileage)
