import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2, 4, 6])

print(f'Поэлементное умножение массивов {array1 * array2}')
print(f'Возведение в степень {np.power(array1, array2)}')
print(f'Деление на скаляр {array1 / 5, array2 / 2}')