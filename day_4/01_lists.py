# ---------------------------------------------------------
# DAY 4 | TOPIC 1: LISTS — Storing Many Values 📝
# A list is an ordered collection that can hold many items.
# Lists are MUTABLE — you can change them after creation.
# ---------------------------------------------------------


# 1. CREATING A LIST
print("--- Creating a list ---")
fruits = ["apple", "banana", "cherry", 1 , True]
print(fruits)


# 2. ACCESSING ITEMS BY INDEX
print("\n--- Accessing items ---")
print(fruits[0])   # first item
print(fruits[1])   # second item
print(fruits[-1])  # last item


# 3. CHANGING AN ITEM (mutable!)
print("\n--- Changing an item ---")
fruits[1] = "mango"
print(fruits)


# 4. ADDING ITEMS
print("\n--- Adding items ---")
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "grape")
print("After insert at 1:", fruits)


# 5. REMOVING ITEMS
print("\n--- Removing items ---")
fruits.remove("cherry")
print("After remove 'cherry':", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("After pop:", fruits)


# 6. LIST LENGTH
print("\n--- List length ---")
print(len(fruits))


# 7. FINDING INDEX AND COUNT
print("\n--- Index and count ---")
print("Index of 'mango':", fruits.index("mango"))
print("Count of 'apple':", fruits.count("apple"))


# 8. SORTING AND REVERSING
print("\n--- Sort and reverse ---")
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)


# 9. SLICING A LIST
print("\n--- Slicing ---")
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[:3])
print(nums[2:])


# 10. CHECKING IF AN ITEM EXISTS
print("\n--- Checking membership ---")
if "mango" in fruits:
    print("Mango is in the list!")
