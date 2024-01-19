import numpy as np

data = np.random.randint(100, size = 100)

summ = np.sum(data)

print(f"Среднее значение равно {summ/data.size}")

print(f"Медиана {np.median(data)}")

print(f"Отклонение {np.std(data)}")
