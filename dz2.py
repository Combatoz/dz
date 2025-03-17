# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# class Arhiv:
#     arh_num = []
#     arh_text = []
#     def __init__(self, num, text = 'No text'):
#         self.num = num
#         self.text = text
#         self.arh_num.append(num)
#         self.arh_text.append(text)
#
#
# s = Arhiv(3, 'Ihar')
# print(s.num, s.text, s.arh_num, s.arh_text)
# b = Arhiv(4)
# print(s.num, b.num, b.text, s.arh_num,s.arh_text)

class Archive:
    _instance = None
    archive_nums = []
    archive_strings = []

    def __new__(cls, num, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_strings.append(cls._instance.string)
        return super().__new__(cls)

    def __init__(self, num, string):
        self.num = num
        self.string = string
        Archive._instance = self

a = Archive(6, 'gfh')
b = Archive(2, 'od')
c = Archive(8, 'ghjhk')
d = Archive(4, 'tytui')
# print(b.num)
# print(a.num)
# print(c.num)
# print(b.num)