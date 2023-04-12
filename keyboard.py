from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#Кнопка для отправки номера
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(btn)
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
    buttons = [KeyboardButton(str(i)) for i in range(1,10)]
    back = KeyboardButton('Назад')
    kb.add(*buttons, back)  # *-отпускает скобки


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
    pass
