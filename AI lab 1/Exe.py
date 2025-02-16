# Task 1: Introduction
def introduction():
    print("Welcome to the Python Program Demo!")
    print("In this demo, we will cover various tasks and Python concepts.")

# Task 2: Terminal
def terminal():
    print("This program runs in a terminal and demonstrates basic Python concepts.")
    print("You can run this script in your terminal using the command: python script_name.py")

# Task 3: Python Interpreter
def python_interpreter():
    print("The Python Interpreter executes the code line by line.")
    print("It can be used interactively or for running scripts.")

# Task 4: Variables
def variables():
    # Defining variables
    name = "Alice"
    age = 25
    height = 5.6
    print(f"My name is {name}, I am {age} years old, and I am {height} feet tall.")

# Task 5: Text Editor
def text_editor():
    print("You can write and edit Python code using a text editor like VSCode or PyCharm.")
    print("Once the code is written, save it with a '.py' extension and run it using Python interpreter.")

# Task 6: Functions
def functions():
    def greet(name):
        return f"Hello, {name}!"
    
    # Calling the function
    print(greet("Bob"))

# Task 7: Lists and Tuples
def lists_and_tuples():
    # Creating a list
    fruits = ["Apple", "Banana", "Cherry"]
    # Creating a tuple
    colors = ("Red", "Green", "Blue")
    
    print(f"Fruits: {fruits}")
    print(f"Colors: {colors}")
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"First color: {colors[0]}")

# Task 8: Conditional Statements
def conditional_statements():
    age = 20
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

# Task 9: The For Loop
def for_loop():
    print("Printing numbers from 1 to 5 using a for loop:")
    for i in range(1, 6):
        print(i)

# Task 10: User Input and the While Loop
def user_input_while_loop():
    print("Enter a number (0 to exit):")
    while True:
        user_input = int(input())
        if user_input == 0:
            print("Exiting program.")
            break
        else:
            print(f"You entered: {user_input}")

# Main Program Execution
def main():
    introduction()
    terminal()
    python_interpreter()
    variables()
    text_editor()
    functions()
    lists_and_tuples()
    conditional_statements()
    for_loop()
    user_input_while_loop()


if __name__ == "__main__":
    main()
