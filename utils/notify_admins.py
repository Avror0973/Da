import logging

from aiogram import Dispatcher

from data.config import admins
from keyboards.inline.choice_buttons import choice


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот запущен и готов к работе\nин ща Аллах1", reply_markup=choice)

        except Exception as err:
            logging.exception(err)
