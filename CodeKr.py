# Fixed username and password
correct_username = "admin"
correct_password = "123"

# Function to check login with multiple attempts
def login():
    attempts = 3  # Set the number of allowed attempts
    
    # Loop to allow the user multiple attempts
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Check if both username and password match
        if username == correct_username and password == correct_password:
            print("Login successful!")
            break  # Exit the loop if login is successful
        else:
            attempts -= 1  # Decrease the attempt count
            if attempts > 0:
                print(f"Invalid username or password. You have {attempts} attempts left.")
            else:
                print("Too many failed attempts. Access locked.")

# Call the login function
login()
