import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery


from keyboards.inline.choice_buttons import choice
from keyboards.inline.set_data import vybor
from loader import dp, db


@dp.message_handler(Command("menu"))
async def show_items(message: Message):
    await message.answer(text='Если суши то WaySushi❤️', reply_markup=choice)


@dp.callback_query_handler(text_contains="delivery")
async def new_delivery(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Доставка временно не работает, сорри")  #вот так нужно добавить след кнопку reply_markup=pear_keyboard


@dp.callback_query_handler(text_contains="my_orders")
async def user_orders(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("У вас не было заказов")


@dp.callback_query_handler(text_contains="my_info")
async def user_info(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    user = db.select_user(user_id=call.from_user.id)
    user_data = []
    for i in user[2:]:
        if i == None:
            user_data.append("- нету данных")
        else:
            user_data.append(i)
    await call.message.answer(f"""👤 Имя: {user_data[0]}\n\n📞 Контактный номер:  {user_data[1]}\n\n 📪 Адрес: {user_data[2]}\n\n\nХотите добавить или изменить данные?""", reply_markup=vybor)
