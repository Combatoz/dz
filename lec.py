# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
# # принтим только в учебных целях, а не для реальных задач
#         print(f'Создал {self} со свойствами:\n'f'{self.name = },\t{self.equipment = },\t{self.life= }')
#
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'],name='Стэнц')



# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         print(f'Создал класс {cls}')
#         return instance
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман')
# print('Создаём третий раз')
# u_3 = User(name='Стэнц')


# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')



# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, name: str):
#         self.name = name
#
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')



# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# u_2 = User('Венкман')


# import sys
# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# del u_1
# print(sys.getrefcount(u_2))
# print('Завершение работы')


# class User:
#     """A User training class for demonstrating class
# documentation.
# Shows the operation of the help(cls) and the dander method
# __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#         print(f'Создал {self.name = }')
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
# u_1 = User('Спенглер')
# print(f'Документация класса: {User.__doc__ = }')
# print(f'Документация экземпляра: {u_1.__doc__ = }')
# print(f'Документация метода: {u_1.simple_method.__doc__}')



# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
#
#     def __repr__(self):
#         return f'User({self.name})'
#
# user = User('Спенглер')
# print(user)



class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней- {self.life}'
    def __repr__(self):
        return f'User({self.name}, {self.equipment})'
u_1 = User('Спенглер')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'],
name='Стэнц')
ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
print(f'{ghostbusters}')
print(repr(ghostbusters))
print(f'{ghostbusters = }')
print(*ghostbusters, sep='\n')
