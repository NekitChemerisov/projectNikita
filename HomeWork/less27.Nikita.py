'''
# 1 - Выборка всех столбцов из таблице orders

SELECT * FROM orders;

# 2 - извлечение уникальных данных 

SELECT DISTINCT category FROM products;


# 3 - извлечение пользователей чей баланс выше 1000

SELECT * FROM users WHERE balance > 1000;

# 4 - извлечение зарпалаты в убывающем порядке

SELECT * FROM employees ORDER BY salary DESC;

# 5 - увеличение запрлат на 5 процентов

UPDATE employees 
SET salary = salary * 1.05;

# 6 - 
'''


