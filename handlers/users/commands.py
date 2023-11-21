from aiogram import types
from loader import dp


@dp.message_handler(commands=["id"])
async def cmd_start(message: types.Message):
    await message.answer(f"{message.from_id}")
