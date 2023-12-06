# #Конвертация температуры
var = int(input('Для перевода температуры из Цельсия в Форенгейт напишите - 1, для Форенгейта в Цельсий напишите - 0: '))

def translate(var):
    if var == 1:
        celsius = int(input('Введите температуру в Цельсиях: '))
        fahrenheit = celsius + 33
        print(celsius, 'по Цельсию будет равно', fahrenheit, 'в Форенгейт')
    if var == 0:
        fahrenheit = int(input('Введите температуру в Форенгейтах: '))
        celsius = fahrenheit - 33
        print(fahrenheit, 'по Форенгейту будет равно', celsius, 'по Цельсию')
    else:
        print('Введите 0 или 1')
translate(var)


#НОК для двух чисел
def nod(a, b):
    while b:
        a, b = b, a % b
    return a

def nok(a, b):
    return abs(a * b) // nod(a, b)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(f"Наименьшее общее кратное чисел {num1} и {num2} равно {nok(num1, num2)}")


#Факториал заданного числа
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Введите число: "))
print(factorial(n))


#Расчет ежемесячного платежа по кредите
def calculation(sum, count_mounth):
    one_mounth = sum / count_mounth
    return one_mounth

sum = int(input("Введите сумму займа: "))
count_mounth = int(input("Введите кол-во месяцев, за которые планируете вернуть бабосы: "))

one_mounth = calculation(sum, count_mounth)
print('Ежемесячный платеж составит', one_mounth, 'сроком на', count_mounth, 'мес.')


#Палиндромом
def is_palindrome_number(number):
    str_num = str(number)
    return str_num == str_num[::-1]

number = int(input("Введите число: "))
if is_palindrome_number(number):
    print(number, 'является палиндромом.')
else:
    print(number, 'не является палиндромом.')
