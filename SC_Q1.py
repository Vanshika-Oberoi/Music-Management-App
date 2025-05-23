user_data = {
    "john.doe@example.com": {"password": "john123", "first_name": "John", "last_name": "Doe", "age": 28},
    "jane.smith@example.com": {"password": "jane456", "first_name": "Jane", "last_name": "Smith", "age": 32},
    "alice.jones@example.com": {"password": "alice789", "first_name": "Alice", "last_name": "Jones", "age": 24},
    "bob.brown@example.com": {"password": "bob101", "first_name": "Bob", "last_name": "Brown", "age": 30},
    "charlie.white@example.com": {"password": "charlie202", "first_name": "Charlie", "last_name": "White", "age": 35},
    "diana.green@example.com": {"password": "diana303", "first_name": "Diana", "last_name": "Green", "age": 27},
    "evan.black@example.com": {"password": "evan404", "first_name": "Evan", "last_name": "Black", "age": 29},
    "fiona.red@example.com": {"password": "fiona505", "first_name": "Fiona", "last_name": "Red", "age": 22},
    "george.blue@example.com": {"password": "george606", "first_name": "George", "last_name": "Blue", "age": 26},
    "hannah.yellow@example.com": {"password": "hannah707", "first_name": "Hannah", "last_name": "Yellow", "age": 31}
}

def signup():
    email = input("Enter your email ID: ")
    if email in user_data:
        print("Email ID already exists. Please use a different one.")
        return
    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    
    user_data[email] = {
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    print("Registration successful!")

def signin():
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    if email in user_data and user_data[email]["password"] == password:
        full_name = user_data[email]["first_name"] + " " + user_data[email]["last_name"]
        print(f"Welcome, {full_name}!")
    else:
        print("Invalid email ID or password.")

def main():
    while True:
        print("Menu: 1. Signup 2. Sign-in 3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            signup()
        elif choice == '2':
            signin()
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
