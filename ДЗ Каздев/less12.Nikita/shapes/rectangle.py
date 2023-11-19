import math
class Rectangle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return 2 * math.pi * self.radius
 
r = int(input("Введите радиус круга: "))
obj = circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))