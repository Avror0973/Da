from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from keyboards.inline.choice_consent import consent
from keyboards.inline.choice_buttons import choice
from loader import dp, bot, db
from aiogram.dispatcher import FSMContext
import time
from data.menu_pictures import menu_pics
from data.prices import sushi_price
from handlers.users.order.functions import print_basket
from datetime import datetime


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


# TODO работа с корзиной
@dp.callback_query_handler(text_contains="basket", state="*")
async def show_basket(call: CallbackQuery, state=FSMContext):
    await call.message.delete_reply_markup()
    # Work with state for basket
    data = await state.get_data()
    text = print_basket(data)
    await call.answer(cache_time=60)
    await call.message.answer(text, reply_markup=consent)
    await state.set_state("*")


# TODO Запись выбора пользователя в FSM
@dp.message_handler(text=menu_list, state="*")
@dp.message_handler(text=drink_list, state="*")
async def menu_get(message: Message, state=FSMContext):
    user_choice = message.text  # Выбор пользователя
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


# TODO Работа с количеством выбора
@dp.message_handler(state="quantity")
async def order_quantity(message: Message, state: FSMContext):
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


# TODO Завершение оформления заказа
@dp.callback_query_handler(text_contains="checkout", state="*")
async def checkout_order(call: CallbackQuery, state=FSMContext):
    now = datetime.now()
    user_id = call.from_user.id
    await call.message.delete_reply_markup()
    await call.message.answer('Ваш заказ принят\n'
                              f'Ожидайте нашего курьера к {now.hour+4}:{now.minute}',
                              reply_markup=choice)
    db.new_order(user_id, 'Умар', 'Горячий шик - 2шт', 'Старая 24', '+79990001122', 0)
    await state.finish()


@dp.callback_query_handler(text_contains="otmena", state="*")
async def checkout_order(call: CallbackQuery, state=FSMContext):
    await call.message.delete_reply_markup()
    await call.message.answer('Вы отменили заказ', reply_markup=choice)
    await state.finish()
