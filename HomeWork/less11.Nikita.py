import math
import datetime 
from datetime import date
import random
import time
from datetime import datetime


#01 Программа по вычислению площади круга
'''r = 6
pi = 3.14
S = pi * math.pow(r, 2)
print(f'Площадь круга равна {S}')'''

#02 Проверка на простое число
'''def is_prime(number):
    if number <= 1:
        return False 

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

number1 = 42

if is_prime(number1):
    print(f"{number1} - это простое число.")
else:
    print(f"{number1} - не является простым числом.")'''


#03 функция по вычислени площади треугольника
'''length = int(input('Введите длину треугольника:'))
height = int(input('Введите высоту треугольника:'))

def area_triangle(length, height):
    S = 0.5 * (length * height)
    print(f'Площадь треугольника со сторонами {length} и {height} равна {S}')

area_triangle(length, height)'''


#04 Программа, которая выводит 7 дней от текущей даты
'''current_date7 = datetime.datetime.today() + datetime.timedelta(days=7)
print(f'Через 7 дней будет {current_date7}')'''

#05 Разница между двумя датами
'''first_date = date(2023, 10, 2)
second_date = date(2023, 10, 30)

def delta(first_date, second_date):
    delta = second_date - first_date
    print(delta)

delta(first_date, second_date)'''

#06 Вывод дня недели для заданной даты
'''def input_date(year, mouth, day):
    дата = datetime.date(year, mouth, day)
    day_of_week = дата.strftime("%A")
    return day_of_week

year = int(input("Введите год (например, 2023): "))
mouth = int(input("Введите месяц (1-12): "))
day = int(input("Введите день (1-31): "))

day_of_week = input_date(year, mouth, day)
print(f"День недели для {day}.{mouth}.{year}: {day_of_week}")'''

#07 сделали на уроке

#08 Генератор случайного имени

'''def random_name(rand):
    generic_name = random.shuffle(rand)
    print('Подобранное имя', generic_name)

rand = ['a', 'd', 'o', 12, 55, 'f']
random_name(rand)'''

#09 Выбор случайного победителя
'''vikroty = ['Михаил', 'Роман', 'Алибек', 'Магомед', 'Маша']
print(vikroty[random.randint(0, len(vikroty))])'''

#10 Вывод текущего времени каждую секунду
'''for i in range(60):
       currenttime = time.localtime()
       timestamp = time.strftime('%H:%M:%S', currenttime)
       time.sleep(1)
       print(timestamp)'''

#11 Текущее время
'''def current_time():
    currenttime = time.localtime()
    timestamp = time.strftime('%H:%M:%S:%p', currenttime)
    print(timestamp)

current_time()'''

#12 Не смог