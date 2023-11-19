class Vehicle():
    def __init__(self, model, year):
        self.model=model
        self.year=year

class Car(Vehicle):
    def __init__(self,model,year,fuel_type):
        super().__init__(model,year)
        self.fuel_type=fuel_type

    def print_info(self):
        print(f"Вид транспорта {self.model}, Год выпуска - {self.year}, Вид топлива - {self.fuel_type}")

class Toyota(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def print_info(self):
        print(f"Вид транспорта {self.model}, Год выпуска - {self.year}, Вид топлива - {self.fuel_type}, Модель машины - {self.model_name}, Расход топлива - {self.fuel_efficiency}")


class Ford(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency

    def print_info(self):
        print(f"Вид транспорта {self.model}, Год выпуска - {self.year}, Вид топлива - {self.fuel_type}, Модель машины - {self.model_name}, Расход топлива - {self.fuel_efficiency}")


class Tesla(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency

    def print_info(self):
        print(f"Вид транспорта {self.model}, Год выпуска - {self.year}, Вид топлива - {self.fuel_type}, Модель машины - {self.model_name}, Расход топлива - {self.fuel_efficiency}")


car = Toyota('машина', 1999, 'бензин', 'Тойота', '10 л')
car.print_info()


#2
'''class Animal ():
    def my_abstract_method(self):
        pass

class Flyable():
    def my_abstract_method2(self):
        pass

class Bird(Animal, Flyable):
    def my_abstract_method2(self):
        return super().my_abstract_method2()'''