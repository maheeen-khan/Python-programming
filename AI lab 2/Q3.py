clist = ['Canada', 'USA', 'Mexico', 'Australia']

# 1. Loop that counts from 0 to 100
print("\nCounting from 0 to 100:")
for i in range(101):
    print(i, end=" ")

# 2. Multiplication table (1 to 10)
print("\n\nMultiplication Table :")
for i in range(1, 11):
    print(f"6 x {i} = {6 * i}")

# 3. Numbers from 10 to 1 (backwards)
print("\nNumbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")

# 4. Count all even numbers up to 10
print("\n\nEven numbers up to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")

# 5. Sum of numbers from 100 to 200
total_sum = sum(range(100, 201))
print(f"\n\nSum of numbers from 100 to 200: {total_sum}")
