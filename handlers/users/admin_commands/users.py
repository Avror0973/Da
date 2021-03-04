from aiogram import types

from loader import dp, db
from data.config import admins

@dp.message_handler(commands='users', user_id=admins)
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    count = db.count_users()[0]
    print(count, '^^^^^^^^^^^^^^^^^')
    last_ten = db.select_last_ten_users()
    print(last_ten)
    text = f'Всего пользователей в базе: {count}.\nПоследние 10 пользователей:\n'
    for user in last_ten:
        text += f'👤<a href="tg://user?id={user[1]}">{user[2]}</a>  📱{user[3]} 📍{user[4]}\n'
    await message.answer(text)
    db.select_last_ten_users()


@dp.message_handler(commands='users')
async def get_message(message: types.Message):
    await message.answer("Команда доступна только администраторам бота")