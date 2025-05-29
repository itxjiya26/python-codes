import array

# Create an integer array
marks = array.array('i', [80, 85, 90, 75, 60])

print("Marks array:", marks)

# Accessing elements
print("First mark:", marks[0])

# Adding a new mark
marks.append(95)
print("After appending 95:", marks)

# Removing an element
marks.remove(75)
print("After removing 75:", marks)

# Looping through array
print("All marks:")
for mark in marks:
    print(mark)
