import mysql.connector  # Importing the MySQL connector library for connecting to the MySQL database
from mysql.connector import Error  # Importing the Error class to handle exceptions related to MySQL operations

def connect_to_database():
    # This function establishes a connection to the MySQL database.
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Host where the MySQL database is running (usually 'localhost')
            database='user_registration', # The specific database to connect to
            user='root',    # MySQL username; replace with your MySQL username
            password='12345' # MySQL password; replace with your MySQL password
        )
        if connection.is_connected():
            # If the connection is successful, notify the user
            print("Successfully connected to the database")
            return connection  # Return the connection object to use in other functions
    except Error as e:
        # If there is an error during the connection process, print the error
        print(f"Error: {e}")
        return None  # Return None if the connection fails

def is_valid_email(email):
    # This function checks if the email is valid based on specific criteria.
    allowed_domains = [
        "gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com", 
        "aol.com", "zoho.com", "protonmail.com", "mail.com", "yandex.com",
        "gmx.com", "inbox.com", "live.com", "msn.com", "qq.com", "me.com", 
        "comcast.net", "verizon.net", "att.net", "bellsouth.net"
    ]
    
    # Check if the email contains '@' to split into username and domain
    if '@' not in email:
        return False
    
    username, domain = email.split('@', 1)  # Split the email into username and domain parts

    # Check if the username starts with a letter (not a number or special character)
    if not username[0].isalpha():
        return False

    # Check if username and domain are both present after splitting
    if not username or not domain:
        return False

    # Ensure that the domain contains a dot, indicating a valid format
    if '.' not in domain:
        return False

    # Ensure the domain is in the list of allowed domains
    if domain not in allowed_domains:
        return False

    return True  # If all checks pass, return True (email is valid)

def is_valid_password(password):
    # This function checks if the password meets specific security criteria.
    
    # Check if the password length is between 6 and 16 characters
    if not (5 < len(password) < 17):
        return False

    # Check if the password contains at least one digit
    has_digit = any(char.isdigit() for char in password)
    
    # Check if the password contains at least one uppercase letter
    has_upper = any(char.isupper() for char in password)
    
    # Check if the password contains at least one lowercase letter
    has_lower = any(char.islower() for char in password)
    
    # Check if the password contains at least one special character
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    # Return True only if all conditions are met
    if has_digit and has_upper and has_lower and has_special:
        return True
    else:
        return False  # Return False if any condition is not met

def register_user(connection):
    # This function handles the registration of a new user by inserting their details into the database.
    cursor = connection.cursor()  # Create a cursor object to interact with the database

    first_name = input("Enter first name: ")  # Prompt the user to enter their first name
    last_name = input("Enter last name: ")  # Prompt the user to enter their last name

    # Validate the email until a valid one is provided
    while True:
        email = input("Enter email: ")  # Prompt the user to enter their email
        if is_valid_email(email):
            break  # If the email is valid, exit the loop
        else:
            print("Error: Invalid email format or domain. Please ensure the email does not start with a number or special character and is from the allowed domains.")

    # Validate the password until a valid one is provided
    while True:
        password = input("Enter password: ")  # Prompt the user to enter their password
        if is_valid_password(password):
            break  # If the password is valid, exit the loop
        else:
            print("Error: Password must be 6-16 characters long, include at least one digit, one uppercase letter, one lowercase letter, and one special character. Please try again.")

    try:
        # Insert the user's details into the 'users' table in the database
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, email, password))  # Execute the query with the provided user data
        connection.commit()  # Commit the transaction to save the changes
        print("User registered successfully!")  # Inform the user that registration was successful

    except Error as e:
        # If there is an error during the insertion, print the error and rollback the transaction
        print(f"Error: {e}")
        connection.rollback()

def main():
    # This is the main function that coordinates the connection and registration processes.
    connection = connect_to_database()  # Establish a connection to the database
    if connection:
        register_user(connection)  # If connection is successful, proceed with user registration
        connection.close()  # Close the database connection when done

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
