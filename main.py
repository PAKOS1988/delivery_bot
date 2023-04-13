from botcreat import dp
from aiogram import executor
import keyboard
import states


@dp.message_handler(commands=['start'])
async def start_cmd(message):
    start_txt=f'{message.from_user.first_name}👋\nВас приветствует 🤖 отдел доставки компании DokOutsource'
    start_reg=f'Для начала пройдите простую регистрацию, чтобы в дальнейшем не было проблем с доставкой\n\nВведите Ваше имя или выберите поделиться👇:'
    user_id=message.from_user.id
    user_name=message.from_user.first_name
    print(user_id, user_name)
    await message.answer(start_txt)
    await message.answer(start_reg, reply_markup=keyboard.get_name_kb())
    await states.Reg.get_name.set()

@dp.message_handler(state=states.Reg.get_name)
async def get_name(message, state=states.Reg.get_name):
    if message.text=='Взять из ТГ аккаунта':
        name=message.from_user.first_name
        print(name)
        await state.update_data(user_name=name)
        await message.answer(f'Отлично! {name}👍, теперь нам нужно знать Ваш телефон👇:', reply_markup=keyboard.phone_number_kb())
        await states.Reg.get_contact.set()
    elif message.text != 'Взять из ТГ аккаунта' and message.text.isdigit()==False:
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
        await message.answer(f'Отлично! {name["user_name"]}👍\nВы прошли регистрацию, поздравляем🎉🎉🎉', reply_markup=keyboard.gender_kb())
        await states.Choice.get_product.set()
    else:
        await message.answer(f'Ой! {name["user_name"]}\nВы допустили ошибку при выборе пола, воспользуйтесь кнопкой выбора!', reply_markup=keyboard.products_kb())
        await states.Reg.get_gender.set()


executor.start_polling(dp)

