from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart

from data.config import allowed_users
from loader import dp, bot


lst = ["asd", "ddd", 'fdfdf']


@dp.inline_handler(text="stimorol")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку",
                    parse_mode="HTML"
                ),
            ),
        ],

        cache_time=5)

@dp.inline_handler(text=lst[:3])
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Da vala",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку",
                    parse_mode="HTML"
                ),
            ),
        ],

        cache_time=5)


@dp.inline_handler(text="меню")
async def empty_query(query: types.InlineQuery):
    user = query.from_user.id
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Горячий шик",
                input_message_content=types.InputTextMessageContent(
                    message_text="Хочу горячий шик",
                    parse_mode="HTML"
                ),
                thumb_url="https://avatars.mds.yandex.net/get-altay/1680678/2a0000016a3a9be06c574da331838e5d3f99/XXL",
                description="330 рублей"
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="Бешенный лосось",
                input_message_content=types.InputTextMessageContent(
                    message_text="Хочу бешенный шик",
                    parse_mode="HTML"
                ),
                thumb_url="https://thumb.tildacdn.com/tild6436-6131-4963-a134-663233333130/-/resize/352x/-/format/webp/IMG_9695.jpg",
                description="330 рублей"

            ),
            types.InlineQueryResultArticle(
                id="3",
                title="Банзай 2-я порция",
                input_message_content=types.InputTextMessageContent(
                    message_text="Хочу банзай",
                    parse_mode="HTML"
                ),
                thumb_url="https://sushikoto.ru/wp-content/uploads/2020/01/2020-05-05-13-47-52-e1595417307812.jpg",
                description="600 рублей"
            ),
            types.InlineQueryResultArticle(
                id="4",
                title="Черный самурай",
                input_message_content=types.InputTextMessageContent(
                    message_text="Хочу черный самурай",
                    parse_mode="HTML"
                ),
                thumb_url="https://im0-tub-ru.yandex.net/i?id=e97455c94100a7575295129a485b6b33-l&n=13",
                description="399 рублей"
            ),
            types.InlineQueryResultArticle(
                id="5",
                title="Красивые роллы 2-я порция",
                input_message_content=types.InputTextMessageContent(
                    message_text="Хочу красивые роллы",
                    parse_mode="HTML"
                ),
                thumb_url="https://gdepoest.kz/images/70000001025756659/org/43419272_2088154364612764_735340801785728193_n.jpg",
                description="600 рублей\nДля фотографий самое - то"
            ),
        ],
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены")