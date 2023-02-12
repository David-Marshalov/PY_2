class Сountry:
    """ Базовый класс страна. """

    laws_of_country = {}

    def __init__(self, name_first: str, continents: str, size: int, count_population: int):
        """Конструктор

        name_first - название страны
        continents - континент где расположена страна
        size - размер страны
        count_population - колич населения проживающая в данной стране
        """
        self.name_first = name_first
        self.continents = continents
        self.size = size
        self.count_population = count_population

    @classmethod
    def add_low(self, number_low: int, means_low:str):
        if number_low in Сountry.laws_of_country:
            print("Этот закон уже добавлен в словарь")
        else:
            Сountry.laws_of_country[number_low] = means_low



    def __str__(self)-> str:
        """магический метод для отображения информации об объекте класса для пользователей """
        return f"Страна {self.name_first}. Континент {self.continents}. Рзамер {self.size}. Количество населения {self.count_population}"

    def __repr__(self)-> str:
        """магический метод для отображения информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}(name={self.name_first!r}, Континент={self.continents!r}, Размер={self.size!r}, Количество населения={self.count_population!r})"


class City(Сountry):
    """ Базовый класс город. """
    def __init__(self, name_first: str, continents: str, size: int, count_population: int,  name_city: str, size_city: int, count_population_city: int):
        """Конструктор

        name_city - название города

        size_city - размер города
        count_population_city - колич населения проживающая в данном городе
        """
        super().__init__(name_first, continents, size, count_population)
        self.name_city = name_city
        self.size_city = size_city
        self.count_population_city = count_population_city


    def __str__(self)-> str:
        """магический метод для отображения информации об объекте класса для пользователей """
        return f"Город {self.name_city}. Размер города {self.size_city}. Количество населения {self.count_population_city}."

    def __repr__(self)-> str:
        """магический метод для отображения информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}(name={self.name_city!r}, Размер города={self.size_city!r},  Количество населения={self.count_population_city!r})"



x = City("Россия", "asia", 17098246, 140000000, "Санкт-Петербург", 1439, 5607916)
print(x.__dict__)

Сountry.add_low(123, "ghbf")

City.add_low(12, "dfsfs")

City.add_low(12, "222")

print(City.laws_of_country)