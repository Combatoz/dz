# Задача о матричных операциях
#
# Инструкция по использованию платформы
#
#
#
# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
#
# Атрибуты класса:
#
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
#
# Методы класса:
#
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный список data размером rows x cols и заполняет его нулями.
#
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки. Например:
#
#
# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.
#
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
#
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.
#
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.
#
# Пример
#
# На входе:
#
#
# # Создаем матрицы
# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]
#
# matrix2 = Matrix(2, 3)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]
#
# # Выводим матрицы
# print(matrix1)
#
# print(matrix2)
# На выходе:
#
#
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# На входе:
#
#
# # Сравниваем матрицы
# print(matrix1 == matrix2)
# На выходе:
#
#
# False
# На входе:
#
#
# # Выполняем операцию сложения матриц
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)
# На выходе:
#
#
# 8 10 12
# 14 16 18
# На входе:
#
#
# # Выполняем операцию умножения матриц
# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]
#
# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]
#
# result = matrix3 * matrix4
# print(result)
# На выходе:
#
#
# 25 28
# 57 64
# 89 100

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result.strip()

    def __repr__(self):
        return f"Matrix(rows={self.rows}, cols={self.cols})"

    def __eq__(self, other):
        if self.rows!= other.rows or self.cols!= other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]!= other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum

        return result

# Пример использования
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [4, 5]]

matrix2 = Matrix(2, 2)
matrix2.data = [[7, 8], [10, 11]]
print(matrix1)

print(matrix2*matrix1)