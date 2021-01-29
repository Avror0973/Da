from aiogram import types

from loader import dp, db
from data.config import admins

@dp.message_handler(commands='users', user_id=admins)
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    count = db.count_users()[0]
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'В базе <b>{count}</b> пользователей',
            ]))


@dp.message_handler(commands='users')
async def get_message(message: types.Message):
    await message.answer("Команда доступна только администраторам бота")