from aiogram.dispatcher.filters.state import State,StatesGroup

#Процесс регистрации
class Reg(StatesGroup):
    get_name=State() #Получаем имя
    get_contact=State() #Получаем номер телефона
    get_location=State() #Получаем локацию
    get_gender=State() #Получаем пол

#Процесс выбора товара
class Choice(StatesGroup):
    get_product=State() #Получаем название продукта
    get_counts=State() #Получаем количество


#Процесс работы с Корзиной
class Cart(StatesGroup):
    wait_product = State()
    wait_count = State()


#Процесс оформления заказа
class Order(StatesGroup):
    get_location = State()
    get_pay_type = State()
    get_accept = State()


