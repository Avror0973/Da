choice = {'choice': ['горячий шик', 'рататуй', 'Fanta'],
          'choice_quantity': [2, 4, 5],
          'total_price': [180, 180, 66]}


# choice['choice'].append('пепси')
# print(choice['choice'])
#
# ss = len(choice['choice'])
# print(ss)
#
# for i in range(ss):
#     print(choice['choice'][i])
#
#

def print_basket(data):
    len_all = len(data['choice'])
    text = 'Ваша корзина:\n\n'

    #Вытащенные данные из словаря
    choice = data['choice']
    quantity = data['choice_quantity']
    total = data['total_price']

    # Счетчики
    total_sum = 0
    for item in range(len_all):
        text += f'{choice[item]} {quantity[item]}.шт по {total[item]}\n'
        total_sum += total[item]*quantity[item]
    text += f'\n\nОбщая сумма - {total_sum} рублей'
    return text

(print(print_basket(choice)))