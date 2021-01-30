from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




vybor = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='✔️Да',
                                          callback_data='my_orders'
                                      ),
                                      InlineKeyboardButton(
                                          text='✖️Нет',
                                          callback_data='my_info'
                                      )
                                  ]
                              ])