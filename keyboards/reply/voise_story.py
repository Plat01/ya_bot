from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button1 = KeyboardButton("что такое GPT")
button2 = KeyboardButton("В чем разница между SQL и NoSQL")
button3 = KeyboardButton("Love story")


voice_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
voice_keyboard.add(button1)
voice_keyboard.add(button2)
voice_keyboard.add(button3)
