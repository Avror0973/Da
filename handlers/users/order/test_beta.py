import datetime

from datetime import date, time, datetime


today = date.today()
print(today)  # 2017-05-03
print("{}.{}.{}".format(today.day, today.month, today.year))

current_time = time()
print(current_time)  # 00:00:00

current_time = time(16, 25)
print(current_time)  # 16:25:00

current_time = time(16, 25, 45)
print(current_time)  # 16:25:45

now = datetime.now()
print(now)  # 2017-05-03 11:18:56.239443

print(f'{now.day}.{now.month}.{now.year} время {now.hour + 1}:{now.minute}')
# print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 3.5.2017  11:21

print(now.date())
print(now.time())






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

# def print_basket(data):
#     len_all = len(data['choice'])
#     text = 'Ваша корзина:\n\n'
#
#     #Вытащенные данные из словаря
#     choice = data['choice']
#     quantity = data['choice_quantity']
#     total = data['total_price']
#
#     # Счетчики
#     total_sum = 0
#     for item in range(len_all):
#         text += f'{choice[item]} {quantity[item]}.шт по {total[item]}\n'
#         total_sum += total[item]*quantity[item]
#     text += f'\n\nОбщая сумма - {total_sum} рублей'
#     return text
#
# (print(print_basket(choice)))