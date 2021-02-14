from aiogram import types
from keyboards.inline.choice_buttons import choice
from data.config import admins

from loader import dp


@dp.message_handler(commands='backup', user_id=admins)
async def get_backup(message: types.Message):
    backup_file = open('data/data.txt')
    await message.answer_document(backup_file)
    backup_file.close()

