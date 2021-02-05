from aiogram import types
from loader import dp, bot


price = {"бешенный лосось": 330,
         "горячий шик": 330,
         "банзай": 660,
         "чёрный самурай": 399,
         "красивые роллы": 600}

menu_list = ["Бешенный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]

@dp.message_handler(text=menu_list)
async def Losos(message: types.Message):
    user_choice = message.text
    await message.answer_photo(photo="AgACAgIAAxkBAAILNWAdrs0ycUjUBSKR2vNBODRNbpNyAAKzsTEbu7PwSJYYi-6zsEMmUWiJni4AAwEAAwIAA20AAyJ4AQABHgQ",
                               caption=f"🍣<b>{user_choice}</b>\n"
                                       f"Цена {price['бешенный лосось']}\n"
                                       f"Ингредиенты: Лосось и другое")
