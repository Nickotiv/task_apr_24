class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        return self.width == self.height


rect = Rectangle(4, 5)
print(rect.area())        # 20
print(rect.perimeter())   # 18
print(rect.is_square())   # False

square = Rectangle(3, 3)
print(square.is_square()) # True

r = Rectangle(2, 3)
assert r.area() == 6, "Ошибка: площадь 2x3 должна быть 6"
assert r.perimeter() == 10, "Ошибка: периметр 2x3 должен быть 10"
print("Тест 1 пройден")

r1 = Rectangle(5, 5)
r2 = Rectangle(5, 6)
assert r1.is_square() == True, "Ошибка: квадрат 5x5 должен давать True"
assert r2.is_square() == False, "Ошибка: прямоугольник 5x6 должен давать False"
print("Тест 2 пройден")
