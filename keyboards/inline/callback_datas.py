from aiogram.utils.callback_data import CallbackData


user_info_callback = CallbackData("yes_set", "no_set")
menu_callback = CallbackData("delivery", "my_orders", "my_info")
consent_callback = CallbackData("yes", "no", "cancel")