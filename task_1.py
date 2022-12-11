import doctest
class Book:
    def __init__(self, author: str):
        self.author = author
        self.last_read_page = 0
        self.pages = 500
        self.notices = []
        """
                Создание и подготовка к работе объекта "Книга"
                :param author: Автор
        """
        if not isinstance(author, str):
            raise TypeError("Имя автора должен быть типа str")

    def increment_last_read_page(self, read_pages: int) -> None:
        if not isinstance(read_pages, int):
            raise TypeError("Тип количества прочтенных старниц болжен быть int")
        if read_pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        if self.last_read_page + read_pages > self.pages:
            raise ValueError("Вы не могли прочитать больше чем количество страниц в книге")
        self.last_read_page += read_pages

    def add_notice(self, notice: str) -> None:
        if not isinstance(notice, str):
            raise TypeError(" Заметка должена быть типа str")
        self.notices.append("notice")




class Employee:
    """Базовый класс для всех сотрудников
    :raise TypeError:если имя  не типа str будет вызывать ошибку
    """
    emp_count = 0

    def __init__(self, name: str, salary)->None:
        if not isinstance(name, str):
            raise TypeError("Тип  болжен быть str")
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self) ->float:
        print('Всего сотрудников: %d' % Employee.emp_count)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


class Point:
    """Задаем точки в пространстве

    :raise TypeError:если значение точки в пространстве не будет типа int будет вызывать ошибку
    :raise TypeError:если имя и  цвет не типа str будет вызывать ошибку
    """
    color = 'red'
    circle = 2

    def __init__(self, x : int, y : int)->float:
        if not isinstance(x, int):
            raise TypeError("Тип  болжен быть int")
        if not isinstance(y, int):
            raise TypeError("Тип  болжен быть int")
        self.x = x
        self.y = y

    def __init__(self, name: str, color: str )->str:
        if not isinstance(name, str):
            raise TypeError("Тип  болжен быть str")
        if not isinstance(color, str):
            raise TypeError("Тип  болжен быть str")
        self.name = name
        self.color = color

point = Point("Dava", "green")
print(point.__dict__)


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
