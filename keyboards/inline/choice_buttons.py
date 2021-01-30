from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




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