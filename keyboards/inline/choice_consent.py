from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




consent = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Суши 🍣',
                                          switch_inline_query_current_chat="суши"
                                      ),
                                      InlineKeyboardButton(
                                          text="🍹 Напитки",
                                          switch_inline_query_current_chat="напитки"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='💵 Оформить заказ',
                                          callback_data="checkout"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='🛑 Отменить заказ',
                                          callback_data='otmena'
                                      )
                                  ]
                              ])