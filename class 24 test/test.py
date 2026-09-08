# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Dictionary created with at least 5 student name-score pairs  →   5 marks
# 2.  A loop correctly calculates and prints the class average      →  10 marks
# 3.  Highest and lowest scores and students identified             →  10 marks
# 4.  .get() used to look up student — friendly message if missing  →  10 marks
# 5.  Program runs without any errors                               →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================


students = {"maya": 95, "ava": 84, "henry": 76, "jane": 65, "cody": 54}
qwerty = 0
for i in students:
    qwerty += students[i]
average = qwerty / 5
print(average)
highest_score = max("maya")
lowest_score = min("cody")
students.get("maya")
print(highest_score)
print(lowest_score)
qwwqqw = str(input("enter students name to foind how much they got."))
print(students.get(qwwqqw))

