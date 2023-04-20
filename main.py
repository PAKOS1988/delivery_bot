import botcreat

from botcreat import dp
from aiogram import executor
import keyboard
import states
import DB
from aiogram.types import CallbackQuery, Message
count=0
prod_par=[]
@dp.message_handler(commands=['start'])
async def start_cmd(message):
    start_txt=f'{message.from_user.first_name}👋\nВас приветствует 🤖 отдел доставки компании DokOutsource'
    start_reg=f'Для начала пройдите простую регистрацию, чтобы в дальнейшем не было проблем с доставкой\n\nВведите Ваше имя или выберите поделиться👇:'
    user_id=message.from_user.id
    user_name=message.from_user.first_name
    print(user_id, user_name)
    cheker = DB.get_user_id(user_id)
    if user_id==1268659822:

        await message.answer('Приветствую, хозяин. Что вас привело в бот?', reply_markup = keyboard.administration())
        await states.Admin.get_status.set()
    elif cheker:

        await message.answer('Выберите продукт', reply_markup = keyboard.products_kb())

    else:
        await message.answer(start_txt)
        await message.answer(start_reg, reply_markup=keyboard.get_name_kb())
        await states.Reg.get_name.set()

@dp.message_handler(state=states.Admin.get_status)
async def get_name(message, state=states.Admin.get_status):
    if message.text=='Редактировать продукты':
        await message.answer(f'{message.from_user.first_name}, какую операцию вы хотите совершить?>>', reply_markup=keyboard.admin_pruducts_edit())
        await state.finish()
        await states.Admin_edit_products.get_status.set()
    elif message.text == 'Заказы':
        await message.answer(f'{message.from_user.first_name}, какую операцию вы хотите совершить?>>',
                             reply_markup=keyboard.admin_pruducts_view())
        await state.finish()
        await states.Admin_view_orders.get_status.set()

@dp.message_handler(state=states.Admin_edit_products.get_status)
async def get_name(message, state=states.Admin_edit_products.get_status):
    if message.text=='Добавить🆕':
        await message.answer('Введите наименование товара', reply_markup=keyboard.ReplyKeyboardRemove())
        await states.Add.get_name.set()
    elif message.text == 'Удалить🚮':
        info_prod=DB.get_products_id_name()
        result = 'Ваши товары:\n'
        for i in info_prod:
            result += f'ID = {i[0]}, Наименование: {i[1]}\n'
        await botcreat.bot.send_message(message.from_user.id, text=result)
        await message.answer('Введите ID товара', reply_markup=keyboard.ReplyKeyboardRemove())
        await states.Admin_edit_products.del_product.set()
    elif message.text == 'Редактировать📝':
        info_prod=DB.get_products_id_name()
        result = 'Ваши товары:\n'
        for i in info_prod:
            result += f'ID = {i[0]}, Наименование: {i[1]}\n'
        await botcreat.bot.send_message(message.from_user.id, text=result)
        await message.answer('Введите ID товара', reply_markup=keyboard.ReplyKeyboardRemove())
        await states.Admin_edit_products.edit_product.set()
    elif message.text == 'Вернуться в главное меню🔙':
        await message.answer('Возвращение в главное меню', reply_markup=keyboard.administration())
        await states.Admin.get_status.set()

@dp.message_handler(state=states.Admin_edit_products.del_product)
async def get_name(message, state=states.Admin_edit_products.del_product):
    info_prod=DB.get_products_id_name()
    id_prod=[i[0] for i in info_prod]
    print(id_prod)
    if int(message.text) in id_prod:
        await message.answer('Возвращение в главное меню', reply_markup=keyboard.administration())
        DB.delete_product(int(message.text))
        await states.Admin.get_status.set()

    else:
        await message.answer(f'{message.from_user.first_name}, введите ID товара, который вы хотите удалить?>>')
        await states.Admin_edit_products.del_product.set()
@dp.message_handler(state=states.Admin_edit_products.edit_product)
async def get_name(message, state=states.Admin_edit_products.edit_product):
    info_prod=DB.get_products_id_name()
    id_prod=[i[0] for i in info_prod]
    print(id_prod)
    if int(message.text) in id_prod:
        DB.delete_product(int(message.text))
        await message.answer('Введите наименование товара', reply_markup=keyboard.ReplyKeyboardRemove())
        await states.Add.get_name.set()

    else:
        await message.answer(f'{message.from_user.first_name}, введите ID товара, который вы хотите изменить?>>')
        await states.Admin_edit_products.edit_product.set()
@dp.message_handler(state=states.Add.get_name)
async def prod_name(message, state=states.Add.get_name):
    name=message.text
    print(name)
    await state.update_data(prod_name=name)
    await message.answer(f'Теперь введите стоимость {name}:>>')
    await states.Add.get_price.set()
@dp.message_handler(state=states.Add.get_price)
async def prod_price(message, state=states.Add.get_price):
    price=float(message.text)
    print(price)
    await state.update_data(prod_price=price)
    await message.answer('Теперь введите описание товара:>>')
    await states.Add.get_info.set()

@dp.message_handler(state=states.Add.get_info)
async def prod_price(message, state=states.Add.get_info):
    info=message.text
    print(info)
    await state.update_data(prod_info=info)
    await message.answer('Теперь загрузите фото для товара:>>')
    await states.Add.get_photo.set()

@dp.message_handler(content_types=['photo'],state=states.Add.get_photo)
async def prod_photo(message, state=states.Add.get_photo):
    photo_id=message.photo[-1].file_id
    print(photo_id)
    await state.update_data(prod_photo=photo_id)
    all_info = await state.get_data()
    id=DB.get_products_id()
    id_prod=len(id)+1
    print(id)
    name = all_info.get('prod_name')
    price = all_info.get('prod_price')
    print(price)
    info = all_info.get('prod_info')
    photo = all_info.get('prod_photo')
    DB.add_product(id_prod, name, price, info, photo)
    print(DB.get_products_all(name))
    await message.answer('Отлично! Товар добавлен', reply_markup = keyboard.administration())
    await state.finish()
    await states.Admin.get_status.set()
@dp.message_handler(state=states.Reg.get_name)
async def get_name(message, state=states.Reg.get_name):
    if message.text=='Взять из ТГ аккаунта':
        name=message.from_user.first_name
        print(name)
        await state.update_data(user_name=name)
        await message.answer(f'Отлично! {name}👍, теперь нам нужно знать Ваш телефон👇:', reply_markup=keyboard.phone_number_kb())
        await states.Reg.get_contact.set()
    elif message.text != 'Взять из ТГ аккаунта' and message.text.isdigit() == False:
        print(message)
        name=message.text
        print(name)
        await state.update_data(user_name=name)
        await message.answer(f'Отлично! {name}👍, теперь нам нужно знать Ваш телефон👇:',
                             reply_markup=keyboard.phone_number_kb())
        await states.Reg.get_contact.set()
@dp.message_handler(state=states.Reg.get_contact, content_types=['contact'])
async def get_contact(message, state=states.Reg.get_contact):
        phone_number = message.contact.phone_number
        print(F'Номер телефона: {phone_number}')
        name=await state.get_data()
        await state.update_data(user_contact=phone_number)
        await message.answer(f'Отлично! {name["user_name"]}👍, теперь нам нужно знать Вашу локацию👇:', reply_markup=keyboard.location_kb())
        await states.Reg.get_location.set()

#Обработчик этапа получения локации
@dp.message_handler(state=states.Reg.get_location, content_types=['location'])
async def get_location(message, state=states.Reg.get_location):
        location = (message.location.longitude, message.location.latitude)
        print(f'Локация:{location}')
        name = await state.get_data()
        await state.update_data(user_location=location)
        await message.answer(f'Отлично! {name["user_name"]}👍, теперь нам нужно знать Ваш пол👇:', reply_markup = keyboard.gender_kb())
        await states.Reg.get_gender.set()

@dp.message_handler(state=states.Reg.get_gender, content_types=['text'])
async def get_gender(message, state=states.Reg.get_gender):

    name = await state.get_data()
    if message.text=='Мужской' or message.text=='Женский':
        gender=message.text
        print(f'Пол:{gender}')
        await state.update_data(user_gender=gender)
        await message.answer(f'Отлично! {name["user_name"]}👍\nВы прошли регистрацию, поздравляем🎉🎉🎉', reply_markup=keyboard.products_kb())

    else:
        await message.answer(f'Ой! {name["user_name"]}\nВы допустили ошибку при выборе пола, воспользуйтесь кнопкой выбора!', reply_markup=keyboard.gender_kb())
        await states.Reg.get_gender.set()
    all_info = await state.get_data()
    name = all_info.get('user_name')
    ph_num = all_info.get('user_contact')
    locat = all_info.get('user_location')
    gender = all_info.get('user_gender')
    id = message.from_user.id
    DB.add_user(id,name,ph_num,locat[0],locat[1],gender)
    print(DB.get_user())

# @dp.message_handler(state=states.Cart.wait_products)
# async def cart_products(message, state=states.Cart.wait_products):
#     user_id=message.from_user.id
#     products=DB.get_products_from_carts_user_id(user_id=user_id)
#     print(products)
#     await message.answer(products, reply_markup=keyboard.cart_kb())
#Независимый обработчик текста для основного меню
@dp.message_handler(content_types=['text'])
async def process(message):
    user_answer = message.text
    global count
    count=0

# Список продуктов
    act_products=[i[0] for i in DB.get_products_names()]
    if user_answer=='Корзина':
        #Получить корзину пользователя
        user_products = DB.get_products_from_carts_user_id(message.from_user.id)

        # Проверка корзины на наличие продуктов
        if user_products:
            # Формируем сообщение
            result = 'Ваша корзина:\n'
            for i in user_products:
                result += f'- {i[2]}, Кол-во {i[3]}, Сумма {i[4]}\n'
            await message.answer(result, reply_markup=keyboard.cart_kb())
            await states.Cart.delete_cart.set()
        else:
            await message.answer('Ваша корзина пустая', reply_markup=keyboard.products_kb())
        # await message.answer('Ваша корзина',reply_markup=keyboard.cart_kb())

    elif user_answer=='Оформить заказ':
        await message.answer('Оформление заказа',reply_markup=keyboard.check_order_kb())
        await states.Order.get_location.set()
    elif user_answer in act_products:
        await message.answer(f'Вы выбрали {user_answer} ', reply_markup=keyboard.ReplyKeyboardRemove())
        qwerty=DB.get_products_all(user_answer)
        global prod_par
        prod_par=[]
        print(f'данные с продукта {qwerty}')
        prod_par.insert(0,message.from_user.id)
        prod_par.insert(1,qwerty[0])
        prod_par.insert(2,qwerty[1])
        prod_par.insert(3, qwerty[2])
        print(f'Данные прод-пар {prod_par}')
        await message.answer(f'Укажите количество: {count}', reply_markup=keyboard.count_edit_kb())
        # создать обработчик для сохранения выбранного количества
    else:
        await message.answer('Вы допустили ошибку при выборе', reply_markup=keyboard.products_kb())

@dp.message_handler(state=states.Cart.delete_cart)
async def delete_cart(message, state=states.Cart.delete_cart):
    user_answer=message.text
    user_id=message.from_user.id
    if user_answer=='Очистить заказ':
        DB.delete_products_from_carts_id(user_id)
        await message.answer('Корзина очищена!')
    elif user_answer=='Оформить заказ':
        # Получить корзину пользователя
        user_products = DB.get_products_from_carts_user_id(message.from_user.id)
        # Проверка корзины на наличие продуктов
        if user_products:
            # Формируем сообщение
            result = 'Ваш заказ:\n'
            admin_message = 'Новый заказ:\n'
            for i in user_products:
                result += f'- {i[2]}, Кол-во {i[3]}, Сумма {i[4]}\n'
                admin_message += f'- {i[2]}, Кол-во {i[3]}, Сумма {i[4]}\n'
            await message.answer(result, reply_markup=keyboard.products_kb())
            await message.answer('Успешно оформлено!')
            await state.finish()
            await botcreat.bot.send_message(1268659822,admin_message)
            DB.delete_products_from_carts_id(user_id)
@dp.callback_query_handler(text='count_increase')
async def count_edit_handler(callback: CallbackQuery):
    user_data = await dp.current_state(user=callback.message.chat.id).get_data()
    if user_data.get('count'):
        print(f'текущее количество{user_data.get("count")}')
        count = user_data.get('count')
        await dp.current_state(user=callback.message.chat.id).update_data(count=count + 1)
        user_data = await dp.current_state(user=callback.message.chat.id).get_data()
        count = user_data.get('count')
        print(f'новое количество{user_data.get("count")}')
        await callback.message.edit_text(f'Укажите количество: {count}', reply_markup=keyboard.count_edit_kb())
    else:
        await dp.current_state(user=callback.message.chat.id).update_data(count=1)
        await callback.message.edit_text(f'Укажите количество: 1', reply_markup=keyboard.count_edit_kb())

    print(callback.message.text)

@dp.callback_query_handler(text='count_decrease')
async def count_edit_handler(callback:CallbackQuery):

    user_data = await dp.current_state(user=callback.message.chat.id).get_data()
    if user_data.get('count'):
        print(f'текущее количество{user_data.get("count")}')
        count = user_data.get('count')
        await dp.current_state(user=callback.message.chat.id).update_data(count=count - 1)
        user_data = await dp.current_state(user=callback.message.chat.id).get_data()
        count = user_data.get('count')
        print(f'новое количество{user_data.get("count")}')
        await callback.message.edit_text(f'Укажите количество: {count}', reply_markup=keyboard.count_edit_kb())
    else:
        await dp.current_state(user=callback.message.chat.id).update_data(count=1)

        await callback.message.edit_text(f'Укажите количество: 1', reply_markup=keyboard.count_edit_kb())

@dp.callback_query_handler(text='count_add')
async def count_add_handler(callback: CallbackQuery):
    user_data = await dp.current_state(user=callback.message.chat.id).get_data()
    count=user_data.get('count')
    global prod_par
    prod_par.insert(4,count)
    amount=prod_par[3]*count
    prod_par.insert(5, amount)
    print(prod_par)
    DB.add_product_cart(prod_par[0],prod_par[1],prod_par[2],prod_par[4],prod_par[5])
    await callback.answer(f'Добавлено {prod_par[2]} в количестве {count} шт', show_alert=True)
    await callback.message.answer('Выберите следующий продукт', reply_markup=keyboard.products_kb())
    await callback.message.edit_reply_markup(reply_markup=None)




executor.start_polling(dp)

