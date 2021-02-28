from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from keyboards.inline.choice_consent import consent
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time
from data.menu_pictures import menu_pics
from data.prices import sushi_price


def print_basket(data):
    """Функция которая сортирует по полочкам данные из data которую заполнял пользователь во время оформления заказа"""
    len_all = len(data['choice'])
    text = ''

    #Вытащенные данные из словаря
    choice = data['choice']
    quantity = data['choice_quantity']
    total = data['total_price']

    # Счетчики
    total_sum = 0

    if len_all != 0:
        text += '<b>Ваша корзина:</b>\n\n'
        for item in range(len_all):
            text += f'<i>{item+1}) {choice[item]} {quantity[item]}.шт по {total[item]}₽</i>\n'
            total_sum += total[item]*quantity[item]
        text += f'\n\nОбщая сумма - {total_sum}₽'

    else:
        text += 'Ваша корзина пуста'
    return text

menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]
drink_list = ['Coca Cola', 'Fanta', 'Lipton', 'Lipton - Лимон', 'Pepsi']



@dp.callback_query_handler(text_contains="menu")
async def get_menu(call: CallbackQuery, state=FSMContext):
    # Удаление предыдущей инлайн клавиатуры
    await call.message.delete_reply_markup()
    await call.answer(cache_time=60)
    # Создание стейта со словарем для хранения информации
    await state.update_data(choice=[], choice_quantity=[], total_price=[])
    await call.message.answer("Выбирайте📲", reply_markup=consent)


@dp.callback_query_handler(text_contains="basket", state="*")
async def show_basket(call: CallbackQuery, state=FSMContext):
    await call.message.delete_reply_markup()\
    # TODO работа с корзиной

    # Work with state for basket
    data = await state.get_data()
    text = print_basket(data)
    await call.answer(cache_time=60)
    await call.message.answer(text, reply_markup=consent)


@dp.message_handler(text=menu_list, state="*")
@dp.message_handler(text=drink_list, state="*")
async def menu_get(message: Message, state=FSMContext):
    user_choice = message.text  # Выбор пользователя

    # TODO Запись выбора пользователя в FSM
    # Получаем словарь из стейта и обрабатываем его
    data = await state.get_data()
    data_choice = data.get('choice')
    data_choice.append(user_choice)
    # print(data_choice)
    await state.update_data(choice=data_choice)

    # Отвечаем пользователю
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    await message.answer_photo(photo=f"{menu_pics[user_choice]}",
                               caption=f"🍣<b>{user_choice}</b>\n"
                                       f"Цена {sushi_price[user_choice]}₽\n"
                                       f"Ингредиенты: недоступно\n")
    # await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
    await message.answer("Введите количество")
    await state.set_state("quantity")



@dp.message_handler(state="quantity")
async def order_quantity(message: Message, state: FSMContext):
    # TODO Работа с количеством выбора
    if message.text.isdigit():
        data = await state.get_data() # вытаскиваем данные из стейта

        # Переменные с FSM
        choice = data.get('choice') # Вытаскиваем список с выбором пользователя
        choice_quantity = data.get('choice_quantity') # вытаскиваем список с количеством
        choice_total = data.get('total_price') # Вытаскиваем список с общей суммой для каждой позиции

        # Другие переменные
        quantity = int(message.text)  # сообщение пользователя
        total_sum = sushi_price[choice[-1]]

        # Обновление данных списков для последующей записи в FSM
        choice_quantity.append(quantity) #Обновление списка с кол-ом
        choice_total.append(total_sum) #Обновление списка с общей суммой

        await state.update_data(choice_quantity=choice_quantity, total_price=choice_total) # Обновляем значение словаря в стейте
        data2 = await state.get_data()

        answer_message = print_basket(data2)
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        await message.answer(answer_message)
        await message.answer("Еще чего ни будь?", reply_markup=consent)
        await state.set_state("*")
        # await state.finish()

    else:
        await message.answer("Введите количество цифрами")
        await state.set_state("quantity")