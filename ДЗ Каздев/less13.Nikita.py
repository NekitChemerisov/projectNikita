#02 Создать класс Person
'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee (Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_info(self):
        print(f'Человека зовут {self.name}, его возраст {self.age}, его зарплата составляет {self.salary}')

pers1 = Employee('Sasha', 22, '5500$')
pers2 = Employee('Mikhail', 49, '10500$')

pers1.get_info()
pers2.get_info()'''

#03
'''class Animal():
    def speak():
        return 1

class Dog(Animal):
    def speak(self):
        return "Гав"


class Cat(Animal):
    def speak(self):
        return "Мяу"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())'''

#04 Разработать класс BankAccount
'''class BankAccount():
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number) 
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return self.balance

savings_account = SavingsAccount()'''



