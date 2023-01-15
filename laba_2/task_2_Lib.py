from task_1_Book import Book
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


# TODO написать класс Library

class Library():
    """Класс для работы с библиотекой"""

    def __init__(self, books = None):
        """
        Метод конструктор
        :param books: название книги
        """
        if  books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
Если книг в библиотеке нет, то вернуть 1.
Если книги есть, то вернуть идентификатор последней книги увеличенный на 1."""
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self,  id_):
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса."""

        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
