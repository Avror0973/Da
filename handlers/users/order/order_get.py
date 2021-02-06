from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
import time

# Прайс меню
price = {"Бешеный лосось": 330,
         "Горячий шик": 330,
         "Банзай": 600,
         "Чёрный самурай": 399,
         "Красивые роллы": 600}

# file_id фотографий
menu_pics = {"Бешеный лосось": "AgACAgIAAxkBAAILNWAdrs0ycUjUBSKR2vNBODRNbpNyAAKzsTEbu7PwSJYYi-6zsEMmUWiJni4AAwEAAwIAA20AAyJ4AQABHgQ",
            "Горячий шик": "AgACAgIAAxkBAAILfmAeRbosSvpCeYmpRb0_b7s89gc8AAIKsTEbqH3xSNsmO3Q5ymQUm7rRly4AAwEAAwIAA3gAA1V9BgABHgQ",
            "Банзай": "AgACAgIAAxkBAAILgGAeRdX3fTK3JMCPIzybMuSiEd_8AAILsTEbqH3xSCOsxXXOysS8gwvkly4AAwEAAwIAA3gAA22qBgABHgQ",
            "Чёрный самурай": "AgACAgIAAxkBAAILgmAeRzPy9-maSaEHs1FTwmZ1nr9WAAIMsTEbqH3xSNg7Dwz9vkCq6qDoly4AAwEAAwIAA3gAAxqqBgABHgQ",
            "Красивые роллы": "AgACAgIAAxkBAAILhGAeR087FZOO6_ilBriCzXuvckvCAAINsTEbqH3xSFS-lxKOQRQVWy4lmy4AAwEAAwIAA3gAA3xTAgABHgQ"}

menu_list = ["Бешеный лосось", "Горячий шик", "Банзай", "Чёрный самурай", "Красивые роллы"]

user_order = [] # Добавляем выбранное блюдо сюда

@dp.message_handler(text=menu_list)
async def menu_get(message: types.Message, state=FSMContext):
    quantity = 1 # Количество
    user_choice = message.text # Выбор пользователя
    user_order.append(user_choice)
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", ) # эффект "печатает"
    time.sleep(0.5)
    await message.answer_photo(photo=f"{menu_pics[user_choice]}",
                               caption=f"🍣<b>{user_choice}</b>\n"
                                       f"Цена {price[user_choice] * quantity}₽\n"
                                       f"Ингредиенты: Лосось и другое\n")
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", ) # эффект "печатает"
    time.sleep(0.5)
    await message.answer("Введите количество")
    await state.set_state("quantity")


@dp.message_handler(state="quantity")
async def order_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    user_choice = user_order[0]
    if quantity.isdigit():
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        time.sleep(0.5)
        await message.answer(f"<b>Ваш заказ:</b>\n"
                             f"{user_order[0]} - {price[user_choice]}₽\n"
                             f"Количество - {quantity}\n"
                             f"Итоговая стоимость заказа - {int(quantity) * price[user_choice]}₽")
        await bot.send_chat_action(chat_id=message.chat.id, action="typing", )  # эффект "печатает"
        time.sleep(0.5)
        await message.answer("Мы вам позвоним для подтверждения заказа")
        await state.finish()
    else:
        await message.answer("Введите количество цифрами")
        await state.set_state("quantity")

