import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.choice_buttons import choice

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer("Добро пожаловать в наш бот", reply_markup=choice)
    except sqlite3.IntegrityError as err:
        print(err)
        await message.answer("Рад что ты вернулся", reply_markup=choice)
    # count = db.count_users()[0]
    # await message.answer(
    #     "\n".join(
    #         [
    #             f'Привет, {message.from_user.full_name}!',
    #             f'Ты был занесен в базу',
    #             f'В базе <b>{count}</b> пользователей',
    #         ]))
