from aiogram import types, Dispatcher
import json
import string
from create_bot import dp


# @dp.message_handler()
async def bed_words_stop(message: types.Message):
    if{i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
    .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Мат запрещён!')
        await message.delete()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(bed_words_stop)

