# 1. Access items in a list
students = ["Ali", "Ayesha", "Bilal", "Zara"]
print("First student:", students[0])         
print("Last student:", students[-1])         

# 2. Use loops with lists
print("\nAll students using for loop:")
for student in students:
    print(student)

# 3. Add items to a list
students.append("Usman")                    # Adds at the end
students.insert(2, "Fatima")                # Inserts at index 2
print("\nList after adding students:", students)

# 4. Remove items from a list
students.remove("Ayesha")                   # Removes by value
popped_student = students.pop()             # Removes last item
print("\nList after removing students:", students)
print("Popped student:", popped_student)

# 5. Sort a list
marks = [85, 70, 92, 60, 78]
marks.sort()
print("\nSorted marks:", marks)

# 6. Copy a list
students_copy = students.copy()
print("\nCopied list of students:", students_copy)

# 7. List comprehension
#  create a list of square marks
squared_marks = [m * m for m in range(1, 6)]
print("\nList of squares using list comprehension:", squared_marks)
