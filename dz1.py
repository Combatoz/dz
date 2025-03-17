# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import datetime
class MyStr(str):

    def __new__(cls, text = 'No text', author = 'Anonymous'):
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = datetime.datetime.now()
        return instance


s = MyStr('fdksljkfdsf', 'Ihar')
print(s, s.author, s.time)
b = MyStr()
print(b, b.author, b.time)
