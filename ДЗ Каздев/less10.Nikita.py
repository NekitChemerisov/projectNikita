#1 Жанры кино
'''genre = {
    "Комедия": ["1+1", "Маска", "Джентльмены удачи"],
    "Боевик": ["Джон Уик", "Матрица", "Гладиатор"],
    "Ужасы": ["Оно", "Пила", "Сияние"]
}


def update_genre(genre_name, genre_value):
    genre[genre_name] = genre_value
    print(genre)

update_genre('боевик', 'джеки') '''

#2 Список студентов
'''students = {
    'Иван': {'Информатика': 98, 'Математика': 80, 'Физика': 60},
    'Мария': {'Информатика': 93, 'Математика': 75, 'Физика': 55},
    'Алексей': {'Информатика': 66, 'Математика': 85, 'Физика': 70}
}

def find_average_grades(students_dict):
    average_grades = {}
    for student, grades in students_dict.items():
        average = sum(grades.values()) / len(grades)
        average_grades[student] = average
    return average_grades

average_grades = find_average_grades(students)
for student, average in average_grades.items():
    print(f'Средний балл {student}: {average:.2f}')

find_average_grades(students)'''


#Матрица с операцией умножения
'''n = 3  
m = 3  
counter = 1 
matrix = [[counter + m * i + j for j in range(m)] for i in range(n)]
scalar = 2
scaled_matrix = [[element * scalar for element in row] for row in matrix]
for row in scaled_matrix:
    print(row)'''

#Работа с координатами
'''x = 10
y = 20
z = 30
coordinates = [x, y, z]

def coordinates_sum():
    coordinates_1 = tuple(coordinates)
    sum = 0
    for coordinate in coordinates_1:
        sum += coordinate
    print(sum)

coordinates_sum()'''

