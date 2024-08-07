from Connection import *

def register(name, url, username, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''INSERT INTO password (
        name, url, username, password, description)
        VALUES (?, ?, ?, ?, ?)'''
        data = (name, url, username, password, description)
        cursor.execute(sql_statement, data)
        connection.commit()
        connection.close()
        return 'Registration successful'
    except Error as err:
        return 'An error has occurred ' + str(err)

def show():
    data = []
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''SELECT * FROM password'''
        cursor.execute(sql_statement)
        data = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred ' + str(err))
    return data

def search(id):
    data = []
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''SELECT * FROM password WHERE id=?'''
        cursor.execute(sql_statement, (id,))
        data = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred ' + str(err))
    return data

def modify(id, name, url, username, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''UPDATE password SET name=?, url=?,
        username=?, password=?, description=? WHERE id=?'''
        data = (name, url, username, password, description, id)
        cursor.execute(sql_statement, data)
        connection.commit()
        connection.close()
        return 'Password updated successfully'
    except Error as err:
        return 'An error has occurred ' + str(err)

def delete(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_statement = '''DELETE FROM password WHERE id=?'''
        cursor.execute(sql_statement, (id,))
        connection.commit()
        connection.close()
        return 'Password deleted successfully'
    except Error as err:
        return 'An error has occurred ' + str(err)
