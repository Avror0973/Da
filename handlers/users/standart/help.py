from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from data.config import admins


@dp.message_handler(CommandHelp(), user_id=admins)
async def bot_help(message: types.Message):
    await message.answer("<b>Команды для админов</b>:\n"
                         "/users - кол-во пользователей\n"
                         "/message - рассылка\n\n"
                         "<b>Команды для всех</b>\n"
                         "/help - инструкции по использованию бота\n"
                         "/menu - меню\n")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Список команд: </b>",
            "/start - Начать работу",
            "/help - Получить справку",)
    
    await message.answer("\n".join(text), parse_mode='HTML')
