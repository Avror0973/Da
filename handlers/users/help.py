from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать работу",
            "/help - Получить справку",
            "\n<b>Команды для админов:</b>",
            "/users - кол-во пользователей в боте",
            "/message - отправить сообщение пользователям бота")
    
    await message.answer("\n".join(text), parse_mode='HTML')
