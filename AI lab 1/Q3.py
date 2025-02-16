my_list = [10, 20, 30, 40, 50]

# Append a value to the list
my_list.append(60)
print("After append:", my_list)

# Insert a value at a specific position
my_list.insert(2, 25)
print("After insert:", my_list)

# Remove a specific value from the list
my_list.remove(40)
print("After remove:", my_list)

# Pop the last value from the list
last_item = my_list.pop()
print("After pop:", my_list)
print("Popped item:", last_item)

# Reverse the list
my_list.reverse()
print("After reverse:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sort:", my_list)

# Count occurrences of a value
count = my_list.count(30)
print("Count of 30:", count)

# Find the index of a value
index = my_list.index(30)
print("Index of 30:", index)

# Extend the list with another list
my_list.extend([70, 80])
print("After extend:", my_list)

# Clear all elements from the list
my_list.clear()
print("After clear:", my_list)
