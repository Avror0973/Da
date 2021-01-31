import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.choice_buttons import choice

from utils.misc import rate_limit
from loader import dp, db, bot


@rate_limit(5)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo="AgACAgIAAxkBAAIG9WAVlSC_yvWHgX0qWMrN81ELAAGl1AACmLIxG4n-sUiuG0io_4PTNVT6GpguAAMBAAMCAAN4AANzUQYAAR4E",
                             caption="Добро пожаловать в наш бот",
                             reply_markup=choice)
    except sqlite3.IntegrityError as err:
        print(err)
        await message.answer("Рад что ты вернулся", reply_markup=choice)
