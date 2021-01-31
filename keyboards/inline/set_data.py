from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




vybor = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='✔️Да',
                                          callback_data='yes_set'
                                      ),
                                      InlineKeyboardButton(
                                          text='✖️Нет',
                                          callback_data='no_set'
                                      )
                                  ]
                              ])