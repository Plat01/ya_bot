from aiogram import types
from loader import dp
from keyboards.reply import voice_keyboard
from data import static


@dp.message_handler(commands=["voice"])
async def cmd_start(message: types.Message):
    await message.reply("Выберите один из вариантов:", reply_markup=voice_keyboard)


@dp.message_handler(lambda message: message.text == "что такое GPT")
async def handle_gpt_question(message: types.Message):
    # Send a voice message related to "что такое GPT"
    with open(static.VOICE_GPT, 'rb') as voice_file:
        await message.reply_voice(voice=voice_file)


@dp.message_handler(lambda message: message.text == "В чем разница между SQL и NoSQL")
async def handle_sql_nosql_question(message: types.Message):
    # Send a voice message related to "В чем разница между SQL и NoSQL"
    with open(static.VOICE_SQL, 'rb') as voice_file:
        await message.reply_voice(voice=voice_file)


@dp.message_handler(lambda message: message.text == "Love story")
async def handle_love_story_question(message: types.Message):
    # Send a voice message related to "Love story"
    await message.reply_voice(voice="URL_TO_YOUR_VOICE_MESSAGE.mp3")
