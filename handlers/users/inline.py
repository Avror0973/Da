from aiogram import types

from loader import dp



@dp.inline_handler(text=["суши"])
async def sushi_menu(query: types.InlineQuery):
    user = query.from_user.id
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Горячий шик",
                input_message_content=types.InputTextMessageContent(
                    message_text="Горячий шик",
                    parse_mode="HTML"
                ),
                thumb_url="https://avatars.mds.yandex.net/get-altay/1680678/2a0000016a3a9be06c574da331838e5d3f99/XXL",
                description="180 рублей"
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="Бешеный лосось",
                input_message_content=types.InputTextMessageContent(
                    message_text="Бешеный лосось",
                    parse_mode="HTML"
                ),
                thumb_url="https://thumb.tildacdn.com/tild6436-6131-4963-a134-663233333130/-/resize/352x/-/format/webp/IMG_9695.jpg",
                description="180 рублей"

            ),
            types.InlineQueryResultArticle(
                id="3",
                title="Банзай",
                input_message_content=types.InputTextMessageContent(
                    message_text="Банзай",
                    parse_mode="HTML"
                ),
                thumb_url="https://sushikoto.ru/wp-content/uploads/2020/01/2020-05-05-13-47-52-e1595417307812.jpg",
                description="250 рублей"
            ),
            types.InlineQueryResultArticle(
                id="4",
                title="Черный самурай",
                input_message_content=types.InputTextMessageContent(
                    message_text="Чёрный самурай",
                    parse_mode="HTML"
                ),
                thumb_url="https://im0-tub-ru.yandex.net/i?id=e97455c94100a7575295129a485b6b33-l&n=13",
                description="250 рублей"
            ),
            types.InlineQueryResultArticle(
                id="5",
                title="Красивые роллы",
                input_message_content=types.InputTextMessageContent(
                    message_text="Красивые роллы",
                    parse_mode="HTML"
                ),
                thumb_url="https://gdepoest.kz/images/70000001025756659/org/43419272_2088154364612764_735340801785728193_n.jpg",
                description="300 рублей"
            ),
        ],
    )


@dp.inline_handler(text=["напитки"])
async def sushi_menu(query: types.InlineQuery):
    user = query.from_user.id
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Coca Cola",
                input_message_content=types.InputTextMessageContent(
                    message_text="Coca Cola",
                    parse_mode="HTML"
                ),
                thumb_url="https://ешь-суши.рф/assets/images/products/232/coca-cola-0-5.jpg",
                description="105 рублей\nОбъём 0.45л"
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="Fanta",
                input_message_content=types.InputTextMessageContent(
                    message_text="Fanta",
                    parse_mode="HTML"
                ),
                thumb_url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5fdf5e82734197.5d2665b61fe38.png",
                description="80 рублей\nОбъём 0.33л"

            ),
            types.InlineQueryResultArticle(
                id="3",
                title="Lipton - чёрный чай",
                input_message_content=types.InputTextMessageContent(
                    message_text="Lipton",
                    parse_mode="HTML"
                ),
                thumb_url="https://cdn1.ozone.ru/multimedia/1021760524.jpg",
                description="120 рублей\nОбъём 0.8л"
            ),
            types.InlineQueryResultArticle(
                id="4",
                title="Lipton - лимон",
                input_message_content=types.InputTextMessageContent(
                    message_text="Lipton - Лимон",
                    parse_mode="HTML"
                ),
                thumb_url="https://mangal-viborg.ru/img/16783277_1920.jpg",
                description="120 рублей\nОбъём 0.8л"
            ),
            types.InlineQueryResultArticle(
                id="5",
                title="Pepsi",
                input_message_content=types.InputTextMessageContent(
                    message_text="Pepsi",
                    parse_mode="HTML"
                ),
                thumb_url="https://pbs.twimg.com/tweet_video_thumb/CUv3vIaUsAQY20F.png",
                description="80 рублей\nОбъём 0.33л"
            ),
        ],
    )