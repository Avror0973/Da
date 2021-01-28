from aiogram import types

from loader import dp, db, bot


@dp.message_handler(commands='message')
async def get_message(message: types.Message):
    name = message.from_user.full_name
    count = db.count_users()[0]
    msg = db.select_all_users()
    # await message.answer(
    #     "\n".join(
    #         [
    #             f'Попробуем!',
    #             f'В базе <b>{count}</b> пользователей',
    #         ]))
    print(msg)
    count2 = 0
    stop_bot = 0
    for i in msg:  # рассылка сообщения пользователям из БД
        try:
            await bot.send_message(chat_id=i[0], text="Тестовая рассылка")
            count2 += 1
        except:
            stop_bot += 1
    print(count2)
    print(stop_bot)
    await message.answer(f"""Отправлено {count2} пользователям из {count} пользователей""")