from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins
from loader import dp, db, bot
from keyboards.inline.choice_buttons import choice



@dp.message_handler(commands='message', user_id=admins)
async def get_message(message: types.Message, state: FSMContext):
    await message.answer("Пришли сообщение которое нужно разослать пользователям из БД\nДля отмены рассылки нажмите /cancel")
    await state.set_state("message")

@dp.message_handler(commands='message')
async def get_message(message: types.Message, state: FSMContext):
    await message.answer("Команда доступна только администраторам бота", reply_markup=choice)


@dp.message_handler(state="message")
async def send_messages(message: types.Message, state: FSMContext):
    message_text = message.text
    count = db.count_users()[0]
    users = db.select_all_users()
    print(users)
    count2 = 0
    stop_bot = 0
    print(message)
    if message_text == '/cancel':
        await message.answer("Рассылка отменена", reply_markup=choice)
        await state.finish()
    else:
        for i in users:  # рассылка сообщения пользователям из БД
            try:
                await bot.send_message(chat_id=i[1], text=message_text)
                count2 += 1
            except:
                stop_bot += 1
        await message.answer(f"""Отправлено {count2} пользователям из {count} пользователей""", reply_markup=choice)
    await state.finish()