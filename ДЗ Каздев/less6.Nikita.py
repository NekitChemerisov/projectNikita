#Запрос оценки с выдачей результата
result = int(input("Введите свою оценку: "))
if 1 <= result <= 10:
    if 1 <= result <= 3:
        print("Плохо")
    if 4 <= result <= 6:
        print("Удовлетворительно")
    if 7 <= result <= 9:
        print("Хорошо")
    if result == 10:
        print("Отлично")
else:
    print("Введите оценку от 1 до 10")

#Запрос времени с выводом о времени суток
time = int(input("Введите ваше время: "))
if 0 <= time <= 24:
    if 0 <= time <= 6:
        print("Спокойной ночи!")
    if 6 <= time <= 12:
        print("Доброе утро!")
    if 12 <= time <= 18:
        print("Добрый день!")
    if 18 <= time <= 24:
        print("Добрый вечер!")
else:
    print("В сутках 24 часа")

#Все числа, которые делятся на 3 
num = int(input("Введите число: "))
for i in range (1 , num):
    if i % 3 == 0:
        print(i)

#среднеарифметическое всех чисел в списке
numbers = [1, 2, 3, 4, 5]
sum = 0

for num in numbers:
    sum += num

avg = sum / len(numbers)

print("Среднее арифметическое:", avg)

#Елочка
height = int(input("Введите высоту елочки: "))

for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))

print(' ' * (height - 1) + '*')


#Бабочка
size = int(input("Введите размер половины бабочки: "))

for i in range(1, size + 1):
    print('*' * i + ' ' * (2 * (size - i)) + '*' * i) # Верхняя половина бабочки

for i in range(size, 0, -1):
    print('*' * i + ' ' * (2 * (size - i)) + '*' * i) # Нижняя половина бабочки


#Шахматная доска
rows = [
        'rnbqkbnr',
        'pppppppp',
        '........',
        '........',
        '........',
        '........',
        'PPPPPPPP',
        'RNBQKBNR'
    ]
    
for row in rows:
    for char in row:
        print(char, end=' ')
    print()  # Переход на новую строку после вывода строки доски
