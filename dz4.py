# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Arhiv:
    arh_num = []
    arh_text = []
    def __init__(self, num, text = 'No text'):
        self.num = num
        self.text = text
        self.arh_num.append(num)
        self.arh_text.append(text)

    def __str__(self):
        '''info for user'''
        return f'Number: {self.num}, Text: {self.text}, Arhiv: {list(zip(self.arh_num,self.arh_text))}'

    def __repr__(self):
        '''info for programmer'''
        return f'For prog: {self.num}, {self.text}'


s = Arhiv(3, 'Ihar')
print(s.num, s.text, s.arh_num, s.arh_text)
b = Arhiv(4)
print(s.num, b.num, b.text, s.arh_num,s.arh_text)
print(s)
print(repr(s))