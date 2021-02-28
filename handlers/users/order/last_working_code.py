from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from keyboards.inline.choice_consent import consent
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time
from data.menu_pictures import menu_pics
from data.prices import sushi_price


menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]
drink_list = ['Coca Cola', 'Fanta', 'Lipton', 'Lipton - Лимон', 'Pepsi']



@dp.callback_query_handler(text_contains="menu")
async def get_menu(call: CallbackQuery, state=FSMContext):
    # Удаление предыдущей инлайн клавиатуры
    await call.message.delete_reply_markup()
    await call.answer(cache_time=60)
    # Создание стейта со словарем для хранения информации
    await state.update_data(choice=['Горячий шик'], choice_quantity=[], total_price=[])
    # await state.update_data(choice={'choice_food': ['Горячий шик'], 'choice_quantity': [], 'total_price': []})
    await call.message.answer("Выбирайте📲", reply_markup=consent)


@dp.callback_query_handler(text_contains="basket")
async def show_basket(call: CallbackQuery, state=FSMContext):
    await call.message.delete_reply_markup()\
    # TODO работа с корзиной
    # Work with state for basket
    data = await state.get_data()

    user_choice = data.get('choice')
    user_choice.append('sushi')
    await state.update_data(choice=user_choice)
    data2 = await state.get_data()
    print(data2)
    # print(data['choice_food'])
    #
    # data = await state.get_data()
    # choice = data.get('choice')

    await call.answer(cache_time=60)
    await call.message.answer("Ваша корзина пуста", reply_markup=consent)


@dp.message_handler(text=menu_list)
@dp.message_handler(text=drink_list)
async def menu_get(message: Message, state=FSMContext):
    user_choice = message.text  # Выбор пользователя

    # Запись в FSM or Redis
    await state.update_data(choice=user_choice)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    await message.answer_photo(photo=f"{menu_pics[user_choice]}",
                               caption=f"🍣<b>{user_choice}</b>\n"
                                       f"Цена {sushi_price[user_choice]}₽\n"
                                       f"Ингредиенты: недоступно\n")
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    await message.answer("Введите количество")
    await state.set_state("quantity")



@dp.message_handler(state="quantity")
async def order_quantity(message: Message, state: FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        quantity = message.text
        choice = data.get('choice')
        choice_price = sushi_price[choice]
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        await message.answer("<b>Ваш заказ:</b>\n\n"
                             f"{choice} {quantity}шт {choice_price}₽\n\n"
                             f"Общая стоимость заказа {int(quantity) * choice_price}₽", parse_mode='HTML')
        await message.answer("Еще чего ни будь?", reply_markup=consent)
        await state.finish()
    else:
        await message.answer("Введите количество цифрами")
        await state.set_state("quantity")