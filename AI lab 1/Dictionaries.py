my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Using the 'keys()' method to get all the keys
print("Keys:", my_dict.keys())

# Using the 'values()' method to get all the values
print("Values:", my_dict.values())

# Using the 'items()' method to get all key-value pairs
print("Items:", my_dict.items())

# Using the 'get()' method to access a value by key
print("Get 'age':", my_dict.get('age'))

# Using the 'pop()' method to remove a key-value pair by key
removed_item = my_dict.pop('city')
print("Removed item:", removed_item)
print("Dictionary after pop:", my_dict)

# Using the 'update()' method to add or modify a key-value pair
my_dict.update({'age': 30, 'country': 'USA'})
print("Dictionary after update:", my_dict)

# Using the 'clear()' method to remove all items
my_dict.clear()
print("Dictionary after clear:", my_dict)
