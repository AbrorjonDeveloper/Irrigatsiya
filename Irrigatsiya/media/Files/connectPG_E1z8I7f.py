# coding=utf-8
HOST = 'localhost'
USER = 'postgres'
PASS = '7672'
from psycopg2 import connect
def create_database():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    CREATE DATABASE market
                    ''')
    con.close()
    print('ishadi...')
def create_table():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = 'market'
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    CREATE TABLE products(
                            id serial PRIMARY KEY,
                            fname VARCHAR(50),
                            address VARCHAR(150)
                            )
                    ''')
    con.close()
    print('ishadi...')
def get_data():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = 'market'
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    SELECT * FROM products
                    ''')
    print(cursor.fetchall())
    con.close()
    print('ishadi...')
def add_data():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = 'market'
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    INSERT INTO products(fname,address) VALUES('Nurbek','Chilonzor')
                    ''')
    con.close()
    print('ishadi...')
def del_data():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = 'market'
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    DELETE FROM products WHERE id = 4
                    ''')
    con.close()
    print('ishadi...')
def update_data():
    con = connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = 'market'
    )
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute('''
                    UPDATE products SET fname = 'Sarvar', address = 'Sergeli' WHERE id = 3
                    ''')
    con.close()
    print('ishadi...')

update_data()