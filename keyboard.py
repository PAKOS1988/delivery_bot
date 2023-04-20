from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import DB
#Кнопка для отправки номера
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(btn)
    return kb

#Кнопка добавления товара для администратора
def administration():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn_add_product = KeyboardButton('Редактировать продукты')
    btn_orders = KeyboardButton('Заказы')

    kb.add(btn_add_product,btn_orders)
    return kb

def admin_pruducts_edit():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    btn_add_product = KeyboardButton('Добавить🆕')
    btn_del_product = KeyboardButton('Удалить🚮')
    btn_edit_product = KeyboardButton('Редактировать📝')
    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_add_product, btn_del_product)
    kb.add(btn_edit_product)
    kb.add(btn_back)
    return kb

def admin_pruducts_view():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    btn_all_products_view = KeyboardButton('Все заказы по очереди📋')
    btn_id_client_view = KeyboardButton('Все заказы клиента по ID')
    btn_del_order = KeyboardButton('Удалить заказ клиента по ID')
    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_all_products_view, btn_id_client_view, btn_del_order,btn_back)
    return kb
#Кнопка изьятия имени с данных аккаунта
def get_name_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Взять из ТГ аккаунта')
    kb.add(btn)
    return kb

# Кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Поделиться локацией', request_location=True)
    kb.add(btn)
    return kb
# Кнопка для отправки пола
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Мужской')
    btn2 = KeyboardButton('Женский')
    kb.add(btn1,btn2)
    return kb

#Кнопки для выбора количества
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = KeyboardButton('Назад')
    done = KeyboardButton('Добавить в корзину')
    kb.add(back,done)  # *-отпускает скобки
    return kb

#Кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton('Очистить заказ')
    btn2 = KeyboardButton('Оформить заказ')
    btn3 = KeyboardButton('Редактировать')
    btn4 = KeyboardButton('Назад')
    kb.add(btn1,btn2,btn3,btn4)
    return kb

#Кнопки при выборе способа оплаты
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton('Терминал')
    btn2 = KeyboardButton('Наличные')
    btn3 = KeyboardButton('Назад')
    kb.add(btn1, btn2, btn3)
    return kb

#Кнопки для подтверждения заказа
def check_order_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Подтвердить')
    btn2 = KeyboardButton('Отменить')
    btn3 = KeyboardButton('Назад')
    kb.add(btn1, btn2, btn3)


#Кнопки с названиями товаров
def products_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    cart = KeyboardButton('Корзина')
    order = KeyboardButton('Оформить заказ')
    all_products = DB.get_products_names()
    #Генерируем список кнопок с названиями
    btns = [KeyboardButton(i[0]) for i in all_products]
    print(*btns)
    kb.add(*btns)
    kb.add(cart,order)
    return kb

def count_edit_kb():
    kb=InlineKeyboardMarkup(row_width=2)
    btn1=InlineKeyboardButton('-', callback_data='count_decrease')
    btn2 = InlineKeyboardButton('+', callback_data='count_increase')
    btn3 = InlineKeyboardButton('Добавить в корзину', callback_data='count_add')
    kb.add(btn1,btn2,btn3)
    return kb

