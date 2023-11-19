#Вывод четных чисел от 0 до 20
for i in range(21):
     if i % 2 == 0:
         print(i)

#Таблица умножения для числа n
n = int(input(" Введите число: "))
for i in range(11):
     print (n, " * ", i, " = ", n * i )

#Кол-во букв в слове Python
string = "Python"
for letter in string:
     print(letter)

#Сумма четных числе от 0 до 100
sum = 0
num = 1
while num <=100:
     sum += num
     num += 2
print(sum)

#Вывод четных чисел от 0 до введеного числа
n = int(input(" Введите число: "))
for i in range(n + 1):
     if i % 2 == 0:
         print(i)

#Получить число и получить сумму всех чисел в этом числе
sum = 0
num = 1
n = int(input(" Введите число: "))
while num <= n:
    sum += num
    num += 1
print(sum)

#Елочка из *
for i in range(6):
    print(i * "*")

#Таблица умножения от 1 до 5
n = 1
for i in range(1, 6):
     print (n, " * ", i, " = ", n * i )


#1-ое задание со звездочкой
n = int(input(" Введите число: "))
for i in range(n + 1):
     if i % 2 == 0:
         print(i)