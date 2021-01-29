from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.choice_buttons import choice

from loader import dp, db



@dp.message_handler(Command("email"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой имейл\nДля отмены нажми на /cancel")
    await state.set_state("email")



@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    if email == '/cancel':
        await message.answer("Действие отменено", reply_markup=choice)
        await state.finish()
    else:
        db.update_user_email(email=email, id=message.from_user.id)
        user = db.select_user(id=message.from_user.id)
        await message.answer(f"Данные обновлены. Запись в БД: {user}", reply_markup=choice)
        await state.finish()


@dp.message_handler(Command("number"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой номер телефона\nДля отмены нажми на /cancel")
    await state.set_state("number")


@dp.message_handler(state="number")
async def enter_email(message: types.Message, state: FSMContext):
    number = message.text
    if number == '/cancel':
        await message.answer("Действие отменено", reply_markup=choice)
        await state.finish()
    else:
        db.update_user_number(number=number, id=message.from_user.id)
        user = db.select_user(id=message.from_user.id)
        await message.answer(f"Данные обновлены. Запись в БД: {user}", reply_markup=choice)
        await state.finish()
