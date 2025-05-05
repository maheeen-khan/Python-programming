import random
import heapq
from collections import deque

# --- Search Algorithms ---

def random_search(lst, target):
    attempts = 0
    visited = set()
    while attempts < len(lst):
        index = random.randint(0, len(lst) - 1)
        if index not in visited:
            print(f"Trying index {index}...")
            if lst[index] == target:
                return index
            visited.add(index)
            attempts += 1
    return -1

def bfs_closed_list(lst, target):
    visited = set()
    queue = deque(range(len(lst)))
    while queue:
        index = queue.popleft()
        if lst[index] == target:
            return index
        visited.add(index)
    return -1

def dfs_open_list(lst, target):
    stack = list(range(len(lst) - 1, -1, -1))  # reverse order to simulate DFS
    visited = set()
    while stack:
        index = stack.pop()
        if lst[index] == target:
            return index
        visited.add(index)
    return -1

def uniform_cost_search(lst, target):
    pq = []
    visited = set()
    for i in range(len(lst)):
        heapq.heappush(pq, (i, i))  # cost = index (as a dummy cost)
    while pq:
        cost, index = heapq.heappop(pq)
        if index in visited:
            continue
        if lst[index] == target:
            return index
        visited.add(index)
    return -1

# --- Main Program ---

def main():
    print("Enter a list of numbers separated by spaces:")
    user_input = input("> ")
    lst = list(map(int, user_input.strip().split()))

    print("Enter the number to search:")
    target = int(input("> "))

    print("\nChoose search method:")
    print("1. Random Search")
    print("2. BFS (with Closed List)")
    print("3. DFS (with Open List)")
    print("4. Uniform Cost Search")

    choice = input("> ")

    index = -1
    if choice == "1":
        index = random_search(lst, target)
    elif choice == "2":
        index = bfs_closed_list(lst, target)
    elif choice == "3":
        index = dfs_open_list(lst, target)
    elif choice == "4":
        index = uniform_cost_search(lst, target)
    else:
        print("Invalid choice.")
        return

    if index != -1:
        print(f"\n Number {target} found at index {index}.")
    else:
        print(f"\n Number {target} not found in the list.")

if __name__ == "__main__":
    main()
