
grades = {
    "Alice": 88,
    "Bob": 73,
    "Charlie": 91,
    "Diana": 84,
    "Ethan": 76,
    "Fiona": 95,
}

print("=" * 38)
print("       📚  STUDENT GRADE BOOK")
print("=" * 38)
total = 0
for score in grades.values():
    total += score
average = total / len(grades)
print(f"Average grade: {average:.1f}")
top_student = max(grades, key=grades.get)
bottom_student = min(grades, key=grades.get)
print(f"Top student: {top_student} ({grades[top_student]})")
print(f"Bottom student: {bottom_student} ({grades[bottom_student]})")
name = input("Enter a student name: ")
score = grades.get(name)
if score is not None:
    print(f"{name}'s score is {score}")
else:
    print(f"Sorry, {name} was not found in the grade book.")
