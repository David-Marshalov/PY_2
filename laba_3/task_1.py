class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        """магический метод для отображения информации об объекте класса для пользователей """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """магический метод для отображения информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:
        """проверка типа вводимых данных"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типом int")
        self._pages = new_pages


    def __str__(self):
        """магический метод для отображения информации об объекте класса для пользователей """
        return f"Книга {self.name}. Автор {self.author}. Страниц{self.pages!r}."

    def __repr__(self):
        """магический метод для отображения информации об объекте класса в режиме отладки """
        return f"Книга {self.name!r}. Автор {self.author!r}. Страниц{self.pages!r}."


class AudioBook(Book):
    """Аудио формат книги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def pages(self, new_duration) -> None:
        """проверка типа вводимых данных"""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудио книги  должно быть типом float")
        self._duration = new_duration

    def __str__(self):
        """магический метод для отображения информации об объекте класса для пользователей """
        return f"Книга {self.name}. Автор {self.author}. Продолжительность{self.duration!r}."

    def __repr__(self):
        """магический метод для отображения информации об объекте класса в режиме отладки """
        return f"Книга {self.name!r}. Автор {self.author!r}. Продолжительность{self.duration!r}."

