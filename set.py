# Program: Demonstrate Common Set Methods in Python

# 1. Create initial set of students
students = {"Ali", "Zara", "Bilal"}
print("Initial set:", students)

# 2. add(): Add a single item
students.add("Ayesha")
print("After add('Ayesha'):", students)

# 3. update(): Add multiple items
students.update(["Usman", "Fatima"])
print("After update(['Usman', 'Fatima']):", students)

# 4. remove(): Remove a specific item (error if not found)
students.remove("Ali")
print("After remove('Ali'):", students)

# 5. discard(): Remove item (no error if not found)
students.discard("Hamza")   # Hamza not in set, but no error
print("After discard('Hamza'):", students)

# 6. pop(): Remove and return a random item
removed = students.pop()
print(f"Removed by pop(): {removed}")
print("After pop():", students)

# 7. copy(): Create a copy of the set
students_copy = students.copy()
print("Copied set:", students_copy)

# 8. clear(): Remove all items
students.clear()
print("After clear():", students)
print("-" * 40)

# Now demonstrate union, intersection, and difference on two sets
set1 = {"Ali", "Zara", "Bilal"}
set2 = {"Zara", "Bilal", "Usman"}

print("Set1:", set1)
print("Set2:", set2)

# 9. union(): Combine two sets without duplicates
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# 10. intersection(): Common items in both sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# 11. difference(): Items in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)


