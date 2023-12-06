#Разделение и объеденение строк
exec = "Тестовый текст для практического задания"
print(exec.split())


#Замена слов
exec = "Тестовый текст для практического задания"
print(exec.replace("текст", "набор слов")) 


#Извлечение имени пользователя из email адреса
email = "nekit@mail.ru"
print(email[0:5])


#Текстовый калькулятор
room = 10
student = 500
room_people = f"В школе {room} классов и {student} учеников. В каждом классе учится по {student / room} человек"
print(room_people)
