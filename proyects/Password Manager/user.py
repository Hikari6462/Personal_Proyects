import hashlib
from Connection import *

def check_user():
    connection = connect()
    cursor = connection.cursor()
    sql_statement = 'SELECT * FROM user'
    cursor.execute(sql_statement)
    found_user = cursor.fetchall()
    connection.close()
    return found_user

def register(first_name, last_name, master_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''INSERT INTO user
        (first_name, last_name, master_password)
        VALUES (?, ?, ?)'''
        encrypted_mp = hashlib.sha256(master_password.encode('utf-8')).hexdigest()
        data = (first_name, last_name, encrypted_mp)
        cursor.execute(sql_statement, data)
        connection.commit()
        connection.close()
        return 'Registration successful'
    except Error as err:
        return 'An error has occurred ' + str(err)

def check_password(id, master_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''SELECT * FROM user
        WHERE id=? AND master_password=?'''
        encrypted_mp = hashlib.sha256(master_password.encode('utf-8')).hexdigest()
        cursor.execute(sql_statement, (id, encrypted_mp))
        data = cursor.fetchall()
        connection.close()
        return data
    except Error as err:
        return 'An error has occurred ' + str(err)





