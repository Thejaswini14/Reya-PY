# Step 1: Create student_data, a dictionary holding four students, each with their own nested details.

# Step 2: Create two empty containers - a result dictionary and a seen_keys list.

# Step 3: Loop through every student ID and its details inside student_data.

# Step 4: Build a unique_key from each student's name, class, and subjects.

# Step 5: Check whether that unique_key has already been seen before.

# Step 6: If it is new, remember it and keep that student in result; if not, skip it as a duplicate.

# Step 7: Loop through result and print every unique student, one at a time.




student={"id1": "alice", "id2": "alice", "id3": "reya", "id4": "devitha"}
result = {}
seen_keys = []
for i, j in student.items():
    unique = j
    if unique not in seen_keys:
        seen_keys.append(unique)
        result[i] = j
for i, j in result.items():
    print(i,j)
    