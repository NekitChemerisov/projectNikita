#Задание 02 - не понял суть задания, сделал максимально просто, исходя их описания.
staff = ('Дима', 25, 'Миша', 43, 'Валера', 33)
print(staff)
print('---------------------------------------------------------------------------------')


#Задание 03
my_list = [3, 6, 'element1', 'Dima', 55]
if 6 == my_list[1]:
    my_list.remove(6)
    print(f'Элемент удален, обновленный список {my_list}')
print('---------------------------------------------------------------------------------')


#Задание 04
fruit_list = ['личи', 'банан','яблоко', 'апельсин', 'киви', 'абрикос']
for item in fruit_list:
    if len(item) < 5:
        fruit_list.remove(item)
print(fruit_list) 
print('---------------------------------------------------------------------------------')


#Задание 05 - не понял суть задания, сделал максимально просто, исходя их описания.
students = [(5, 'Дмитрий'), (3, 'Айгерим'), (2, 'Боб'), (4, 'Раджа'), (5, 'Вениамин')]
print(students)
print('---------------------------------------------------------------------------------')


#Задание 06 - 07 объеденил
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = numbers_list[1:21:2]
print(numbers)


summ = 0 #07
for item in numbers:
    summ = summ + item **2
print(summ)
print('---------------------------------------------------------------------------------')


#Задание 08
matrix = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(2) 
    matrix.append(row)

print(matrix)
