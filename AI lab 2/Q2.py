# Part I: Worker Efficiency Evaluation
time_taken = float(input("Enter the time taken (in hours): "))

if 2 <= time_taken < 3:
    print("The worker is highly efficient.")
elif 3 <= time_taken < 4:
    print("The worker is ordered to improve speed.")
elif 4 <= time_taken < 5:
    print("The worker is given training to improve speed.")
else:
    print("The worker has to leave the company.")

# Part II: Username and Password Authentication
correct_passwords = ["abc$123", "ABC$123"]
username = input("\nEnter username: ")
password = input("Enter password: ")

if password.lower() == 'abc$123':  
    print("Welcome!")
else:
    print("I don't know you.")
