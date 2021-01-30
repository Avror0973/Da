from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.choice_buttons import choice

from loader import dp, db



@dp.message_handler(Command("adress"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Пришлите ваш адрес чтобы мы его запомнили и вам "
                         "не приходилось каждый раз его вводить при заказе."
                         "\nДля отмены нажми на /cancel")
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
        user_data = []
        for i in user[1:]:
            if i == None:
                user_data.append("- не добавлен")
            else:
                user_data.append(i)
        text = (
            "<b>Данные обновлены:</b>",
            f"👤 Имя: {user_data[0]}",
            f"📞 Контактный номер: {user_data[1]}",
            f"📪 Адрес: {user_data[2]}"
        )
        await message.answer("\n".join(text), parse_mode='HTML', reply_markup=choice)
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
        user_data = []
        for i in user[1:]:
            if i == None:
                user_data.append("- не добавлена")
            else:
                user_data.append(i)
        text = (
            "<b>Данные обновлены:</b>",
            f"👤 Имя: {user_data[0]}",
            f"📞 Контактный номер: {user_data[1]}",
            f"📪 Адрес: {user_data[2]}"
        )
        await message.answer("\n".join(text), parse_mode='HTML', reply_markup=choice)
        await state.finish()
