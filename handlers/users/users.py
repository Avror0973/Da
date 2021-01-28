from aiogram import types

from loader import dp, db


@dp.message_handler(commands='users')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    count = db.count_users()[0]
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'В базе <b>{count}</b> пользователей',
            ]))