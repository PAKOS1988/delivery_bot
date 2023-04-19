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
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_add = KeyboardButton('Добавить товар')
    btn_client = KeyboardButton('Зайти как клиент')
    kb.add(btn_add,btn_client)
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

