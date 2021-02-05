from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.choice_buttons import choice
from aiogram.types import message, CallbackQuery
from re import match

from loader import dp, db


@dp.callback_query_handler(text_contains="yes_set")
async def new_delivery(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer("Пришли мне своё имя чтобы мы знали как к вам обращаться"
                              "\n\nДля пропуска этого шага нажми на /skip")
    await state.set_state("name")


@dp.message_handler(state="name")
async def enter_email(message: types.Message, state: FSMContext):
    name = message.text
    user_name = message.from_user.full_name
    if name == '/skip':
        await message.answer(f"Ладно, будем звать вас {user_name.capitalize()}")
        db.update_user_name(name=user_name, id=message.from_user.id)
        await message.answer(f"{user_name.capitalize()} ваш номер мы можем узнать?"
                             f"\n\nДля пропуска этого шага можно нажать на /skip")
        await state.set_state("number")

    else:
        db.update_user_name(name=name, id=message.from_user.id)
        await message.answer(f"{name.capitalize()}, теперь нам нужен ваш номер."
                             f"\n\nЕсли не хотите делиться номером нажимайте на ➡️ /skip")
        await state.set_state("number")


@dp.message_handler(state="number")
async def enter_email(message: types.Message, state: FSMContext):
    number = message.text

    if number == '/skip':
        await message.answer("Ну ладно, будем стучаться в дверь)")
        await message.answer("А адрес мы можем узнать?"
                             "\n\n Для пропуска как обычно /skip")
        await state.set_state("adress")

    elif (match(r'[+7]{1}[0-9]{9}', number) and len(number) == 12) or match(r'[8]{1}[0-9]{9}', number) and len(number) == 11:
        db.update_user_number(number=number, id=message.from_user.id)
        await message.answer("Теперь нам нужен ваш адрес.\nБудет приятно если вы укажете вместе с районом."
                             "\n\n Для пропуска нажимай на /skip")
        await state.set_state('adress')

    else:
        await message.answer("Вы ввели номер в неправильном формате\n"
                             "Заполните по образцу ниже: \n"
                             "+79281112233 или 89281112233")
        await state.set_state("number")


@dp.message_handler(state="adress")
async def enter_email(message: types.Message, state: FSMContext):
    adress = message.text
    if adress == '/skip':
        await message.answer("Ну вы даёте😐\nКак мы по вашему должны доставлять еду?", reply_markup=choice)
        await state.finish()

    else:
        db.update_user_email(email=adress, id=message.from_user.id)
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


@dp.callback_query_handler(text_contains="no_set")
async def new_delivery(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Ну ладно(", reply_markup=choice)