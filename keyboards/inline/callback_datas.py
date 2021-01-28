from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy", "item_name", "quantity")
menu_callback = CallbackData("delivery", "my_orders", "my_info")