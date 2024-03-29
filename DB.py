import sqlite3

#Создать/подключиться к базе данных
connection = sqlite3.connect('delivery.db')

#Создаем переводчик, который будет транслировать запросы БД через пайтон
sql = connection.cursor()

#Запрос создания таблицы USERS
# sql.execute('CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT, loc_lat REAL, loc_long REAL, gender TEXT);')

#Запрос создания таблицы PRODUCTS
# sql.execute('CREATE TABLE products (id INTEGER, name TEXT, price REAL, info TEXT, photo TEXT);')


# Создать таблицу КОРЗИНА
# id
# name
# count
#Запрос создания таблицы CARTS
# sql.execute('CREATE TABLE carts (user_id INTEGER, prod_id INTEGER, prod_name TEXT, count INTEGER, amount REAL);')

#Запрос создания таблицы ORDERS
# sql.execute('CREATE TABLE orders (user_id INTEGER, user_name TEXT, user_phone TEXT, user_loclat REAL, user_loclag REAL, prod_id INTEGER, prod_name TEXT, count INTEGER, amount REAL);')

def add_order(user_id, user_name, user_phone, user_loclat, user_loclag, prod_id, prod_name, count, amount):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO orders VALUES (?,?,?,?,?,?,?,?,?);', (user_id, user_name, user_phone, user_loclat, user_loclag, prod_id, prod_name, count, amount))
    connection.commit()

def get_all_orders():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    all_orders = sql.execute('SELECT * FROM orders;')
    return all_orders.fetchall()

def get_user_id_orders(user_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    all_orders = sql.execute('SELECT * FROM orders WHERE user_id=?;', (user_id,))
    return all_orders.fetchall()

def delete_order(user_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    sql.execute('DELETE FROM orders WHERE user_id=?;', (user_id,))
    connection.commit()

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

def delete_product(prod_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    sql.execute('DELETE FROM products WHERE id=?;', (prod_id,))
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

def get_products_id_name():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_names = sql.execute('SELECT id, name FROM products;')
    return products_names.fetchall()

def get_products_id():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_names = sql.execute('SELECT id FROM products;')
    return products_names.fetchall()

def get_products_all(current_product):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    #Запрос для получения данных из базы данных
    products_all = sql.execute('SELECT * FROM products WHERE name=?;', (current_product, ))

    return products_all.fetchone()

#Проверка пользователя на наличие его в базе данных
def get_user_id(user_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM users WHERE id=?;', (user_id, ))
    if cheker.fetchone():
        return True
    else:
        return False
#Поиск ID продукта для добавления в корзину
def get_prod_id(prod_name):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM products WHERE name=?;', (prod_name, ))
    return cheker.fetchone()
# Создать фнкцию добавления в корзину
def add_product_cart(user_id, prod_id, prod_name, count, amount):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    #Добавляем товар в корзину
    sql.execute('INSERT INTO carts VALUES (?,?,?,?,?);', (user_id, prod_id, prod_name, count, amount))
    #Фиксируем любые изменения в корзине
    connection.commit()

# Создать фнкцию получения корзины пользователя
def get_products_from_carts_user_id(user_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    # Запрос для получения данных из базы данных
    products_from_carts = sql.execute('SELECT * FROM carts WHERE user_id=?;', (user_id,))
    print('Процесс отображения товаров пользователя в корзине:')

    return products_from_carts.fetchall()
def get_all_products_from_carts():
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    # Запрос для получения данных из базы данных
    products_from_carts = sql.execute('SELECT * FROM carts;')
    print('Процесс отображения товаров всей корзины:')
    print(products_from_carts.fetchall())
    return products_from_carts.fetchall()

# Создать фнкцию удаления корзины пользователя
def delete_products_from_carts_id(carts_id):
    connection = sqlite3.connect('delivery.db')
    sql = connection.cursor()
    # Запрос для получения данных из базы данных
    sql.execute('DELETE FROM carts WHERE user_id=?;', (carts_id,))
    connection.commit()
