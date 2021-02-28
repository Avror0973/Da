def print_basket(data):
    """Функция которая сортирует по полочкам данные из data которую заполнял пользователь во время оформления заказа"""
    len_all = len(data['choice'])
    text = ''

    #Вытащенные данные из словаря
    choice = data['choice']
    quantity = data['choice_quantity']
    total = data['total_price']

    # Счетчики
    total_sum = 0

    if len_all != 0:
        text += '<b>Ваша корзина:</b>\n\n'
        for item in range(len_all):
            text += f'<i>{item+1}) {choice[item]} {quantity[item]}.шт по {total[item]}₽</i>\n'
            total_sum += total[item]*quantity[item]
        text += f'\n\nОбщая сумма - {total_sum}₽'

    else:
        text += 'Ваша корзина пуста'
    return text