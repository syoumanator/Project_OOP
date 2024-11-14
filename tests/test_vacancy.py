from src.vacancy import Vacancy


def test_vacancy_init(test_vacancy):
    assert test_vacancy.name == "Junior Python Engineer"
    assert test_vacancy.url == "https://hh.ru/vacancy/110646488"
    assert test_vacancy.area == "Минск"
    assert test_vacancy.salary == 150000
    assert test_vacancy.description == "1+ year of professional work experience"


def test_vacancy_validate(test_vacancy_2):
    assert test_vacancy_2.name == "Junior Python Engineer"
    assert test_vacancy_2.url == "https://hh.ru/vacancy/110646488"
    assert test_vacancy_2.area == "Регион отсутствует"
    assert test_vacancy_2.salary == 0
    assert test_vacancy_2.description == "Описание отсутствует"


def test_vacancy_str(test_vacancy, test_vacancy_2):
    assert str(test_vacancy) == (
        "Junior Python Engineer: 1+ year of professional work experience, Регион:Минск, "
        "Зарплата: 150000, Ссылка: https://hh.ru/vacancy/110646488"
    )
    assert str(test_vacancy_2) == (
        "Junior Python Engineer: Описание отсутствует, Регион:Регион отсутствует, "
        "Зарплата: Нет данных, Ссылка: https://hh.ru/vacancy/110646488"
    )


def test_vacancy_comparison(test_vacancy, test_vacancy_2):
    result = test_vacancy < test_vacancy_2
    assert result is False
    result2 = test_vacancy_2 < test_vacancy
    assert result2 is True


def test_create_json(json_data):
    result = Vacancy.create_json(json_data)
    assert len(result) == 3
    assert result[0].name == "Junior Python Developer"
    assert result[0].url == "https://hh.ru/vacancy/110711272"
    assert result[0].area == "Алматы"
    assert result[0].salary == 0
    assert result[0].description == (
        "Basic knowledge of Python or 1 year in a role focused on Python backend "
        "development (perfectly with Django framework). "
    )
