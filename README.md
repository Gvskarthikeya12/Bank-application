User Registration System

This project is a basic User Registration System implemented in Python, utilizing MYSQL as the database for storing user details.The system ensures that provide valid emails and strong passwords before their information is saved.

Features
  -Email Validation
  - Password Validation
  - MySQL Database Integration

Prerequistes
  Python 3.x
  MySQL Server
  MySQL Connector for Python (mysql-connector-python)

Installation:
   - Install the required Python packages

                pip install mysql-connector-python
Setup
Create a MySQL database:
                
                CREATE DATABASE user_registration;
  -Create a table for storing user information
  -Update database credentials: Open the main.py file and update the database connection details

Usage
Run the script:
      
      python main.py

Follow the on-screen prompts:

-Enter your first name, last name, email, and password.
-The script will validate your email and password before registering the user in the database.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any feature additions or bug fixes.

Contact
For any questions or feedback, feel free to reach out to karthikeya.microsoft@gmail.com
