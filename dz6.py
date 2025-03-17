# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self,other):
        return self.square() == other.square()
    def __ne__(self,other):
        return self.square() != other.square()
    def __gt__(self,other):
        return self.square() > other.square()
    def __ge__(self,other):
        return self.square() <= other.square()
    def __lt__(self,other):
        return self.square() < other.square()
    def __le__(self,other):
        return self.square() >= other.square()

a = Pryam(2,5)
b = Pryam(5)

print(f'площадь a равна площади b? {a == b}')
print(f'площадь a не равна площади b? {a != b}')
print(f'площадь a больше площади b? {a > b}')
print(f'площадь a меньше либо равна площади b? {a <= b}')
print(f'площадь a меньше площади b? {a < b}')
print(f'площадь a больше либо равна площади b? {a >= b}')

