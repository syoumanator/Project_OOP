from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("name", "url", "area", "salary", "description")

    def __init__(self, name, url, area, salary, description) -> None:
        self.name = name
        self.url = url
        self.area = area
        self.salary = salary
        self.description = description
        self.__validate()

    def __validate(self) -> None:
        """Метод проверки входных данных"""
        if not self.area:
            self.area = "Регион отсутствует"

        if not self.salary:
            self.salary = 0

        if not self.description:
            self.description = "Описание отсутствует"

    def __str__(self) -> str:
        if self.salary == 0:
            self.salary = "Нет данных"
            return f"{self.name}: {self.description}, Регион:{self.area}, Зарплата: {self.salary}, Ссылка: {self.url}"
        else:
            return f"{self.name}: {self.description}, Регион:{self.area}, Зарплата: {self.salary}, Ссылка: {self.url}"

    @classmethod
    def create_json(cls, vacancies) -> list[Any]:
        """Метод преобразовывает данные JSON в список"""
        list_of_vacancies = []
        for item in vacancies:
            name = item.get("name")
            url = item.get("alternate_url")
            area = item.get("area").get("name")
            if item["salary"] is None:
                salary = 0
            else:
                salary = item.get("salary").get("from")
            description = item.get("snippet").get("requirement")
            list_of_vacancies.append(cls(name, url, area, salary, description))
        return list_of_vacancies

    def __lt__(self, other):
        """Метод сравнивает зарплату и возвращает наибольшую"""
        if self.salary < other.salary:
            return True
        else:
            return False
