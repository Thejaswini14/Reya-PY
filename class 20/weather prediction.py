# Step 1: Create a tuple called weather holding seven values, one for each day of the week.

# Step 2: Set two counters, sunny and rainy, both starting at zero.

# Step 3: Loop through all seven days using their index positions.

# Step 4: Increase rainy by 1 whenever a day's value is 0, and increase sunny by 1 otherwise.

# Step 5: Compare the two final counts once the loop finishes.

# Step 6: Print "Good weather" if sunny is greater than rainy, and "Bad weather" otherwise.




weather = (1, 0, 1, 0, 1, 0, 1)
counter_sunny = 0
counter_rainy = 0
for i in range (0, 7):
    if(weather[i]== 1):
        counter_sunny += 1
    else:
        counter_rainy += 1 
if counter_sunny > counter_rainy:
    print("nice weather")
else:
    print("the weather was gloomy last week")