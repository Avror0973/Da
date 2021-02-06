from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time
from keyboards.inline.choice_consent import consent
from data.menu_pictures import menu_pics
from data.prices import sushi_price



menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]

user_order = []  # Добавляем выбранное блюдо сюда
user_quantity = [] # Добавляем кол-во


@dp.message_handler(text=menu_list)
async def menu_get(message: types.Message, state=FSMContext):
    quantity = 1  # Количество
    user_choice = message.text  # Выбор пользователя
    user_order.append(user_choice)
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    time.sleep(0.5)
    await message.answer_photo(photo=f"{menu_pics[user_choice]}",
                               caption=f"🍣<b>{user_choice}</b>\n"
                                       f"Цена {sushi_price[user_choice] * quantity}₽\n"
                                       f"Ингредиенты: Лосось и другое\n")
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    time.sleep(0.5)
    await message.answer("Введите количество")
    await state.set_state("consent")


@dp.message_handler(state="consent")
async def order_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    user_quantity.append(int(quantity))
    user_choice = user_order[0]
    if quantity.isdigit():
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        time.sleep(0.5)
        await message.answer(f"<b>Ваш заказ:</b>\n"
                             f"{user_order[0]} - {sushi_price[user_choice]}₽\n"
                             f"Количество - {quantity}\n"
                             f"Итоговая стоимость заказа - {int(quantity) * sushi_price[user_choice]}₽")
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        time.sleep(0.5)
        await message.answer("Хотите еще чего ни будь?", reply_markup=consent)
        await state.finish()
    else:
        await message.answer("Введите количество цифрами")
        await state.set_state("quantity")


# @dp.message_handler(state="quantity")
# async def order_quantity(message: types.Message, state: FSMContext):
#     quantity = message.text
#     user_choice = user_order[0]
#     if quantity.isdigit():
#         await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#         time.sleep(0.5)
#         await message.answer(f"<b>Ваш заказ:</b>\n"
#                              f"{user_order[0]} - {price[user_choice]}₽\n"
#                              f"Количество - {quantity}\n"
#                              f"Итоговая стоимость заказа - {int(quantity) * price[user_choice]}₽")
#         await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#         time.sleep(0.5)
#         await message.answer("Мы вам позвоним для подтверждения заказа")
#         await state.finish()
#     else:
#         await message.answer("Введите количество цифрами")
#         await state.set_state("quantity")
