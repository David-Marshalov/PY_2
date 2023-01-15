BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    """Инициализирует список книг"""

    def __init__(self, id_, name, pages):
        """
        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количетсво страниц
        """

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self)-> str:
        """Метод __str__  возвращает строку формата, где "название_книги" берется с помощью атрибута name"""

        return f'Книга "{self.name} "'



    def __repr__(self) -> str:
        """Метод __repr__  возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр."""

        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"







if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
