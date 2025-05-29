def classify_numbers(numbers):
    # Counters for different types of numbers
    counts = {"positive": 0, "zero": 0, "negative": 0}

    # Loop through each number in the list
    for num in numbers:
        if num > 0:
            print(f"{num} is positive")
            counts["positive"] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts["zero"] += 1
        else:
            print(f"{num} is negative")
            counts["negative"] += 1

    # Return the dictionary with counts
    return counts

# Example usage:
numbers_list = [10, -5, 0, 3, -1, 0, 7]
result = classify_numbers(numbers_list)

print("\nCounts:", result)
