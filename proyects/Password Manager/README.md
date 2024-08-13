# Password Manager
This is a command-line-based password manager application that allows users to securely store, manage, and retrieve their passwords. It ensures the safety of sensitive data by using a master password for authentication and provides various functionalities such as adding, viewing, modifying, and deleting passwords.

## Features
* User Registration: New users can register by providing their first name, last name, and a master password.
* Secure Authentication: Users must enter their master password to access the password manager.
* Add Passwords: Store new passwords with details like name, URL, username, password, and a description.
* View All Passwords: Display all stored passwords with the option to mask the actual password values.
* Search Passwords: Retrieve a specific password entry by its ID.
* Modify Passwords: Update the details of an existing password entry.
* Delete Passwords: Remove a password entry from the database.

## How to Use
* Register: On the first run, you will be prompted to register by entering your first name, last name, and a master password.
* Login: After registration, or on subsequent runs, log in using your master password.
* Manage Passwords: Use the menu options to add, view, search, modify, or delete passwords.

## Menu Options
1- Add Password: Add a new password entry.
2- View All Passwords: Display a table of all stored passwords.
3- View a Password: Search for and view a specific password by ID.
4- Modify Password: Update an existing password entry.
5- Delete Password: Delete a password entry.
6- Exit: Close the application.

## Dependencies
tabulate: Used for displaying passwords in a formatted table.
