from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback, menu_callback




# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='🚀Заказать доставку',
                                          callback_data='delivery'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='🛒Мои заказы',
                                          callback_data='my_orders'
                                      ),
                                      InlineKeyboardButton(
                                          text='📝Мои данные',
                                          callback_data='my_info'
                                      )
                                  ],

                                  [
                                      InlineKeyboardButton(
                                          text='🔺WaySushi🔻',
                                          url='https://t.me/waysushi'
                                      )
                                  ]

                              ])