# Step 1: Set total_chores to 4, store it as original_count, and print how many chores are on today's list.

# Step 2: Set up a completed_count counter starting at 0 and a chore_num counter starting at 1.

# Step 3: Start a while loop that keeps running as long as chore_num is less than or equal to total_chores.

# Step 4: Inside the loop, work out the current chore's name from chore_num, then ask if it has been finished.

# Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.

# Step 6: Once the while loop ends, print the completion message, then safely demonstrate an infinite loop's condition, using a break to stop it after 3 rounds.

# Step 7: Print the final chore checklist summary showing chores assigned, completed, and remainin
 
 
total_chores = 4
original_count = total_chores
print("how many chores do you have today",original_count)
completed_count = 0 
chore_num = 1 
while chore_num <= total_chores:
    if chore_num == 1:
        current_chore = "make your bed"   
    elif chore_num == 2:
        current_chore = "get moms phone and give it to her"
    elif chore_num == 3: 
        current_chore = "put clothes for washing"
    else: 
        current_chore = "clean your room"
    answer =input("have you finished your current chore")
    if answer == "yes":
        completed_count = completed_count + 1 
        chore_num += 1 
    