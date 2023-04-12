from aiogram import Bot, Dispatcher
from token_id import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot=Bot(token=TOKEN)
dp=Dispatcher(bot, storage=MemoryStorage())