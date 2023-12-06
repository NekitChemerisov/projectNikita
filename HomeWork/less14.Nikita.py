#Создать класс календарь
'''class Calendar():
    def __init__(self):
        self.task_dict = {}# Инициализируем пустой словарь

    def add_task(self, date, task):
        self.task_dict[date] = task
        print(f"Задача {task} добавлена на {date}")
    
    def del_task(self, date):
        if date in self.task_dict:
            del self.task_dict[date]
            print(f"Задача на {date} удалена")
        else:
            print(f"Задачи на {date} не существует")

    def print_tasks(self):
        for date, task in self.task_dict.items():
            print(f"{date}: {task}")


calendar = Calendar()  
calendar.add_task('2023.05.05', 'Купить продукты')  # Добавляем задачу
calendar.add_task('2023.05.06', 'Купить штаны') 
calendar.print_tasks()  # Выводим список задач
calendar.del_task('2023.05.05')  # Удаляем задачу
calendar.print_tasks()  # Выводим обновленный список задач'''

#Класс InventoryItem дял работы с товарами
'''class InventoryItem():
    
    def __init__(self,product,quantity,price):
        self.productList = {}
        self.product = product
        self.quantity = quantity
        self.price = price

    def add_product(self): #добавить товар в корзину
        self.productList ={"Название":[self.product], "Количество":[self.quantity], "Цена":[self.price]}
        print(f"Товар {self.product} добавлен")
        print(self.productList)


    def sum_product(self): #сумма всех товаров
        sum = 0
        for price in self.productList['Цена']:
            sum += price
        print(f'Общая стоимость товаров в инветаре {sum}')

    def plus_quan(self,plus): #добавить количество для товара
        print(f'Количество товаров увеличено на {plus} осталось {self.productList['Количество'][0] - plus}')

    def minus_quan(self, minus):#убавить количество для товара
        print(f'Количество товаров уменьшено на {minus} осталось {self.productList['Количество'][0] - minus}')

inventoryItem = InventoryItem('Хлеб', 1222, 550)
inventoryItem.add_product()
inventoryItem.sum_product()
minus = int(input('ВВедите колчество на которое вы хотите убавить товар '))
inventoryItem.minus_quan(minus)
plus = int(input('ВВедите колчество на которое вы хотите добавить товар '))
inventoryItem.plus_quan(plus)'''




