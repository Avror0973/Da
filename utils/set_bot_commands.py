from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Перезапустить бота"),
        types.BotCommand("menu", "Главное меню"),
        types.BotCommand("email", "Ввести имейл"),
        types.BotCommand("users", "Кол-во пользователей"),
        types.BotCommand('message', "Рассылка"),
    ])
