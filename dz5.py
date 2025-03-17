# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Pryam:

    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a

    def perimetr(self):
        return self.a * 2 + self.b * 2

    def square(self):
        return self.a * self.b

    def __add__(self, other):
        return self.perimetr()+other.perimetr()
    def __sub__(self, other):
        return abs(self.perimetr()-other.perimetr())


a = Pryam(2,5)
b = Pryam(5)

print(a.perimetr(),a.square())
print(b.perimetr(),b.square())
print(a+b)
print(a-b)
