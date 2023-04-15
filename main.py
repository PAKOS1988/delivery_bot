from botcreat import dp
from aiogram import executor
import keyboard
import states
import DB

@dp.message_handler(commands=['start'])
async def start_cmd(message):
    start_txt=f'{message.from_user.first_name}👋\nВас приветствует 🤖 отдел доставки компании DokOutsource'
    start_reg=f'Для начала пройдите простую регистрацию, чтобы в дальнейшем не было проблем с доставкой\n\nВведите Ваше имя или выберите поделиться👇:'
    user_id=message.from_user.id
    user_name=message.from_user.first_name
    print(user_id, user_name)
    if user_id==1268659822:
        await message.answer('Приветствую, хозяин. Что вас привело в бот?', reply_markup = keyboard.administration())
        await states.Admin.get_status.set()
    else:
        await message.answer(start_txt)
        await message.answer(start_reg, reply_markup=keyboard.get_name_kb())
        await states.Reg.get_name.set()

@dp.message_handler(state=states.Admin.get_status)
async def get_name(message, state=states.Admin.get_status):
    if message.text=='Добавить товар':
        await message.answer('Введите наименование товара', reply_markup=keyboard.ReplyKeyboardRemove())
        await states.Add.get_name.set()
    elif message.text == 'Зайти как клиент':
        start_txt = f'{message.from_user.first_name}👋\nВас приветствует 🤖 отдел доставки компании DokOutsource'
        start_reg = f'Для начала пройдите простую регистрацию, чтобы в дальнейшем не было проблем с доставкой\n\nВведите Ваше имя или выберите поделиться👇:'
        await message.answer(start_txt)
        await message.answer(start_reg, reply_markup=keyboard.get_name_kb())
        await states.Reg.get_name.set()
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
    print(DB.get_products_all())
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
        await states.Choice.get_product.set()
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

executor.start_polling(dp)

