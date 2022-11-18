'''
creando un bot con aiogram
por que pintó!
y es una muestra de lo que se puede hacer en back-end
'''
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

import os

from time import sleep
from dotenv import load_dotenv


'''
importo las variables de entorno
'''

load_dotenv()

bot_token = os.getenv('ACCESS_TOKEN')
bot = Bot(token=bot_token)

dp = Dispatcher(bot)

respuestas = [] 


@dp.message_handler(commands=['inicio','ayuda'])
async def bienvenida(message: types.Message):
    await message.answer('Hola este es mi primer bot!!')
    await message.answer("Este es otro mensaje!!")

@dp.message_handler(commands=['imagen'])
async def bienvenida(message: types.Message):
    await message.answer_photo("https://t2.ea.ltmcdn.com/es/posts/5/2/6/el_pato_como_mascota_20625_600.jpg")
    await message.answer("Sí! es un pato")


@dp.message_handler()
async def echo(message: types.Message):
    if 'somos' in message.text:
        await message.answer('quienes son?')
    else:
        await message.answer(message.text.upper())

executor.start_polling(dp)