from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time
from data.menu_pictures import menu_pics
from data.prices import sushi_price

#
# menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]
#
#
# @dp.message_handler(text=menu_list)
# async def menu_get(message: types.Message, state=FSMContext):
#     user_choice = message.text  # Выбор пользователя
#     await state.update_data(choice = user_choice)
#     await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#     await message.answer_photo(photo=f"{menu_pics[user_choice]}",
#                                caption=f"🍣<b>{user_choice}</b>\n"
#                                        f"Цена {sushi_price[user_choice]}₽\n"
#                                        f"Ингредиенты: Лосось и другое\n")
#     await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#     await message.answer("Введите количество")
#     await state.set_state("quantity")
#
#
# @dp.message_handler(state="quantity")
# async def order_quantity(message: types.Message, state: FSMContext):
#     if message.text.isdigit():
#         data = await state.get_data()
#         quantity = message.text
#         choice = data.get('choice')
#         choice_price = sushi_price[choice]
#         await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#         await message.answer("<b>Ваш заказ:</b>\n\n"
#                              f"{choice} {quantity}шт {choice_price}₽\n\n"
#                              f"Общая стоимость заказа {int(quantity) * choice_price}₽", parse_mode='HTML')
#         await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
#         time.sleep(0.5)
#         await message.answer("Уже готовим")
#         await state.finish()
#     else:
#         await message.answer("Введите количество цифрами")
#         await state.set_state("quantity")
#
#
# @dp.message_handler(state='cancel')
# async def cancel(message: types.Message, state: FSMContext):
#     await message.answer("Заказ отменен")
#     await state.finish()