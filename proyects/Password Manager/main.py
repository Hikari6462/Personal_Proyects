import os
from getpass import getpass
from tabulate import tabulate
from Connection import *
import user
import password

conexion = conectar()
crear_tablas(conexion)

def start():
    os.system('cls')
    check = user.check_user()
    if len(check) == 0:
        print('Welcome, register your information')
        first_name = input('Please enter your first name:')
        last_name = input('Please enter your last name:')
        master_password = getpass('Enter your master password:')
        response = user.register(first_name, last_name, master_password)
        if response == 'Registration successful':
            print(f'Welcome {first_name}')
            menu()
        else:
            print(response)
    else:
        master_password = getpass('Enter your master password:')
        response = user.check_password(1, master_password)
        if len(response) == 0:
            print('Incorrect password')
        else:
            print('Welcome')
            menu()

def menu():
    while True:
        print('Choose one of the following options:')
        print('\t1- Add password')
        print('\t2- View all passwords')
        print('\t3- View a password')
        print('\t4- Modify password')
        print('\t5- Delete password')
        print('\t6- Exit')
        option = input('Enter an option:')
        if option == '1':
            new_password()
        elif option == '2':
            show_passwords()
        elif option == '3':
            search_password()
        elif option == '4':
            modify_password()
        elif option == '5':
            delete_password()
        elif option == '6':
            break
        else:
            print('You did not enter a valid option')

def new_password():
    name = input('Enter name:')
    url = input('Enter the URL:')
    username = input('Enter username:')
    password = input('Enter password:')
    description = input('Enter description:')
    response = Contrasena.register(name, url, username, password, description)
    print(response)

def show_passwords():
    data = Contrasena.show()
    new_data = []
    headers = ['ID', 'NAME', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION']
    for item in data:
        converted = list(item)
        converted[4] = '********'
        new_data.append(converted)
    
    table = tabulate(new_data, headers, tablefmt='fancy_grid')
    print('\t\t\t\tAll Passwords')
    print(table)

def search_password():
    master_password = getpass('Enter your master password:')
    response = user.check_password(1, master_password)
    if len(response) == 0:
        print('Incorrect password')
    else:
        id = input('Enter the ID of the password to search:')
        data = Contrasena.search(id)
        headers = ['ID', 'NAME', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION']
        table = tabulate(data, headers, tablefmt='fancy_grid')
        print('\t\t\t\tAll Passwords')
        print(table)

def modify_password():
    master_password = getpass('Enter your master password:')
    response = user.check_password(1, master_password)
    if len(response) == 0:
        print('Incorrect password')
    else:
        id = input('Enter the ID of the password to modify:')
        name = input('Enter the new name:')
        url = input('Enter the new URL:')
        username = input('Enter the new username:')
        password = input('Enter the new password:')
        description = input('Enter the new description:')
        response = Contrasena.modify(id, name, url, username, password, description)
        print(response)

def delete_password():
    master_password = getpass('Enter your master password:')
    response = user.check_password(1, master_password)
    if len(response) == 0:
        print('Incorrect password')
    else:
        id = input('Enter the ID of the password to delete:')
        response = Contrasena.delete(id)
        print(response)

start()