from aiogram import types
from loader import dp
from data import static


@dp.message_handler(commands=["/photo"])
async def photo(message: types.Message):
    await message.reply("Хочешь получить мое селфи жми /selfy")


@dp.message_handler(commands=["/selfy"])
async def selfy(message: types.Message):
    with open(static.VOICE_SELFY, 'rb') as voice_file:
        await message.reply_voice(voice=voice_file)
