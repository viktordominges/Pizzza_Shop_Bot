from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.client_kb import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Пожалуйста, напишите ему:\nhttps://t.me/Pizzza_Shop_Bot')
        # await message.answer(message.text)


# @dp.message_handler(commands=['working_hours'])
async def working_hours(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 9:00 до 20:00')


# @dp.message_handler(commands=['address'])
async def address(message: types.Message):
    await bot.send_message(message.from_user.id, 'площадь Независимости, 15')


# @dp.message_handler(commands=['menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(working_hours, commands=['Режим_работы'])
    dp.register_message_handler(address, commands=['Адрес'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])






