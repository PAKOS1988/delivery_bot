import sqlite3

#Создать/подключиться к базе данных
connection = sqlite3.connect('delivery.db')

#Создаем переводчик, который будет транслировать запросы БД через пайтон
sql = connection.cursor()

#Запрос создания таблицы USERS
# sql.execute('CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT, loc_lat REAL, loc_long REAL, gender TEXT);')

#Запрос создания таблицы PRODUCTS
# sql.execute('CREATE TABLE products (id INTEGER, name TEXT, price REAL, info TEXT, photo TEXT);')

#Добавляем пользователя в базу данных
def add_user(user_id, user_name, phone_number, lati, longi, gender):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('INSERT INTO users VALUES (?,?,?,?,?,?);', (user_id, user_name, phone_number, lati, longi, gender))

    #Фиксируем любые изменения
    connection.commit()

#Получение данных с базы данных
def get_user():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    users = sql.execute('SELECT * FROM users;')
    return users.fetchall()

#Запрос для удаления из базы данных
def delete_user():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    sql.execute('DELETE FROM users;')
    connection.commit()

def add_product(prod_id, prod_name, prod_price, prod_info, prod_photo):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Добавляем товар
    sql.execute('INSERT INTO products VALUES (?,?,?,?,?);', (prod_id, prod_name, prod_price, prod_info, prod_photo))

    #Фиксируем любые изменения
    connection.commit()

#Получение данных с базы данных
def get_products_names():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_names = sql.execute('SELECT name FROM products;')
    return products_names.fetchall()

def get_products_id():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_names = sql.execute('SELECT id FROM products;')
    return products_names.fetchall()

def get_products_all():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_all = sql.execute('SELECT * FROM products;')
    return products_all.fetchall()



