from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.choice_consent import consent
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time
from data.menu_pictures import menu_pics
from data.prices import sushi_price


menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]
order_choice = {}




@dp.callback_query_handler(text_contains="menu")
async def get_menu(call: CallbackQuery, state=FSMContext):
    await call.message.delete_reply_markup() # Удаление предыдущей инлайн клавиатуры
    await call.answer(cache_time=60)
    await call.message.answer("Выбирайте📲", reply_markup=consent)
    order_choice[call.from_user.id] = []
    print(order_choice)