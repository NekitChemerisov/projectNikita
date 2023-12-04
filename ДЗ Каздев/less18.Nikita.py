'''x = int(input('Введите число: '))
y = int(input('Введите число: '))

def arifmet(x, y):
    ex = x / y
    print(ex)

try:
    arifmet(x, y)
except ZeroDivisionError as e:
    print(f'Мы не делим на ноль')'''

class ValidationError(Exception):
    
    def __init__(self, message="Произошла ошибка в моем приложении"):
        self.message = message
        super().__init__(self.message)

y = input('Введите число: ')

try:
    if y != "" :
        raise ValidationError("Что-то пошло не так")
except ValidationError as e:
    print(f"Ошибка: {e}")