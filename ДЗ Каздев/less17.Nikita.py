from abc import ABC, abstractmethod
'''class Shape():
    def area(self):
        pass
    
class Circle(Shape):
    def area(self, pi, r):
        S = pi * r**2
        return S
    
class Triangle(Shape):
    def area (self, l, w):
        S = 0.5 * (l * w)
        return S
    
asd = Circle()
print(asd.area(3.14, 5))'''

class Drawable(ABC):
    @abstractmethod
    def draw (self):
        print('Рисунок готов')


class Circle(Drawable):
    def draw(self):
        print('рисуем круг')

class Rectangle(Drawable):
    def draw(self):
        print('Рисуем квадрат')

asd = Circle()
asd.draw()