from os import system
from admin import adminMain
from user import mainUser


def main_script():
    print("Press 1: Login as admin")
    print("Press 2: Login as user")
    print("Press 3: Register as a new user")

    choice = input("Please enter your choice: ")

    if choice == "1":
        login_admin()
    elif choice == "2":
        login_user()
    elif choice == "3":
        register_new_user()
    else:
        print("Please enter a correct number next time!")
        main_script()
        
        
        
     
     
     
     
     
     

# ****************************************************************
# ********************** All FUNCTIONS ***************************
# ****************************************************************   
        

# Function to get user input
def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")
    return name, email, phone_number, password

# Function to write user information to a text file
def write_to_file(name, email, phone_number, password):
    with open('DB/users/user_data.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Password: {password}\n")
        file.write("\n")

# Extraction of username and password for login
def extract_username_password(filename):
    usernames = []
    passwords = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            username = lines[i].split(': ')[1].strip()
            password = lines[i + 3].split(': ')[1].strip()
            usernames.append(username)
            passwords.append(password)
    return usernames, passwords

# Function to register a new user
def register_new_user():
    name, email, phone_number, password = get_user_input()
    write_to_file(name, email, phone_number, password)
    input("User data has been saved to 'user_data.txt'")
    main_script()

# Function to handle user login
def login_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    usernames, passwords = extract_username_password('DB/users/user_data.txt')

    if username in usernames and password in passwords:
        print("Login successful!")
        system("clear")
        mainUser()
    else:
        print("Login failed. Please check your username and password.")
        system("clear")
        main_script()


# The rest of your code remains the same
def login_admin():
    user = input("Please enter your admin username: ")
    password = input("Please enter your admin password: ")
    if user == "jarred" and password == "jarred1234":
        print("Admin login successful!")
        system("clear")
        adminMain()
    else:
        print("Admin login failed. Please check your username and password.")
        system("clear")
        main_script()



# Entry point of the script
if __name__ == "__main__":
    main_script()
