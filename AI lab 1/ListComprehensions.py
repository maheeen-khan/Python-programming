sample_list = ['Python', 'is', 'an', 'amazing', 'programming', 'language']

# List comprehension to generate lowercase strings with length greater than five
result = [s.lower() for s in sample_list if len(s) > 5]


print(result)


# second program

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

# Remove the 0th, 4th, and 5th elements using list slicing and excluding the unwanted indices
modified_list = [sample_list[i] for i in range(len(sample_list)) if i not in [0, 4, 5]]


print(modified_list)
