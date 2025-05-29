# Given tuple of students' marks
marks = (70, 85, 90, 75, 60)

# 1. Print first and last elements
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# 2. Unpack tuple into separate variables
m1, m2, m3, m4, m5 = marks
print("Unpacked marks:", m1, m2, m3, m4, m5)

# 3. Create a new tuple by adding 5 to each element
new_marks = (m1 + 5, m2 + 5, m3 + 5, m4 + 5, m5 + 5)

# 4. Print original and new tuples
print("Original marks:", marks)
print("New marks after adding 5:", new_marks)

