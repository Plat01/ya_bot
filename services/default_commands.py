from aiogram import types, Dispatcher

from loader import config


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('about', "Хочешь прочитать небольшой пост обо мне?"),
            types.BotCommand('about', "Хочешь прочитать небольшой пост обо мне?"),

            # types.BotCommand('help', 'Справка'),
            # types.BotCommand('cancel', 'Отмена операции'),
            # types.BotCommand('settings', 'Настройки'),
        ],
        scope=types.BotCommandScopeAllPrivateChats(),
    )
