import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery


from keyboards.inline.choice_buttons import choice
from loader import dp


@dp.message_handler(Command("menu"))
async def show_items(message: Message):
    await message.answer(text='Если суши то WaySushi❤️', reply_markup=choice)


# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
@dp.callback_query_handler(text_contains="delivery")
async def buying_pear(call: CallbackQuery):
    # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    await call.answer(cache_time=60)

    callback_data = call.data

    # Отобразим что у нас лежит в callback_data
    # logging.info(f"callback_data='{callback_data}'")
    # В питоне 3.8 можно так
    logging.info(f"{callback_data=}")

    await call.message.answer("Доставка временно не работает, сорри")  #вот так нужно добавить след кнопку reply_markup=pear_keyboard


@dp.callback_query_handler(text_contains="my_orders")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("У вас не было заказов")

@dp.callback_query_handler(text_contains="my_info")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("👤 Имя: Владелец Ресторанов ВайСушович\n\n📞 Контактный номер:  +7995 955 95 95\n\n 📪 Адрес: г.Грозный, Орзамиева 16")



@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту покупку!", show_alert=True)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

    # Вариант 2 отправки клавиатуры (по API)
    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)