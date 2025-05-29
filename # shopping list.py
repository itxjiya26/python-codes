# Initial shopping list
shopping_list = ["milk", "bread", "eggs", "butter", "juice", "sugar", "salt", "biscuits", "tea", "coffee"]

# 1. Display all items using a loop
print("Current shopping list:")
for item in shopping_list:
    print("-", item)

# 2. Ask user to add a new item
add_item = input("\nDo you want to add a new item? (yes/no): ")

if add_item.lower() == "yes":
    new_item = input("Enter the item you want to add: ")
    shopping_list.append(new_item)
    print(f"{new_item} has been added to the list.")

# 3. Ask user to remove an item
remove_item = input("\nDo you want to remove any item? (yes/no): ")

if remove_item.lower() == "yes":
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from the list.")
    else:
        print("Item not found.")

# 4. Display the updated list
print("\nUpdated shopping list:")
for item in shopping_list:
    print("-", item)