from aiogram.dispatcher.filters.state import State,StatesGroup

#Процесс регистрации
class Reg(StatesGroup):
    get_name=State() #Получаем имя
    get_contact=State() #Получаем номер телефона
    get_location=State() #Получаем локацию
    get_gender=State() #Получаем пол

#Процесс добавления
class Add(StatesGroup):
    get_id=State() #Получаем id
    get_name=State() #Получаем название товара
    get_price=State() #Получаем стоимость
    get_info=State() #Получаем описание
    get_photo = State()  # Получаем фото
class Admin(StatesGroup):
    get_status=State() #Получаем status

class Admin_edit_products(StatesGroup):
    get_status=State() #Получаем status
    del_product=State()
    edit_product=State()

class Admin_view_orders(StatesGroup):
    get_status=State() #Получаем status

#Процесс выбора товара
class Choice(StatesGroup):

    get_counts=State() #Получаем количество


#Процесс работы с Корзиной
class Cart(StatesGroup):
    delete_cart = State()



#Процесс оформления заказа
class Order(StatesGroup):
    get_location = State()
    get_pay_type = State()
    get_accept = State()


