def store_city_data(filename):
    with open(filename, 'w') as file:
        while True:
            city_name = input("Enter city name (or type 'exit' to stop): ")
            if city_name.lower() == 'exit':
                break
            population = input("Enter population: ")
            mayor = input("Enter mayor's name: ")
            
            file.write(f"{city_name},{population},{mayor}\n")
            print("City data saved!\n")


store_city_data("cities.txt")

print("All city data has been saved to cities.txt.")

# 2

def append_message(filename):
    with open(filename, 'a') as file:
        file.write("Now we are AI students\n")
    print("Message appended successfully!")

# Call the function to append message
append_message("student.txt")


