import sqlite3
from sqlite3 import Error

def connect():
    try:
        connection = sqlite3.connect('database.db')
        return connection
    except Error as err:
        print('An error has occurred')

def create_tables(connection):
    cursor = connection.cursor()
    sql_statement1 = '''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        master_password TEXT NOT NULL
    )'''
    sql_statement2 = '''CREATE TABLE IF NOT EXISTS password (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        url TEXT NOT NULL, 
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        description TEXT
    )'''
    cursor.execute(sql_statement1)
    cursor.execute(sql_statement2)
    connection.commit()
