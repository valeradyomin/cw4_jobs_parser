class Vacancy:
    vacancies_objs_lst = []

    def __init__(self, data_from_api):
        """
        Инициализирует объект Vacancy на основе данных из API.

        Аргументы:
            data_from_api (dict): Словарь с данными о вакансии из API.
        """
        self.keyword = data_from_api.get("keyword")
        self.title = data_from_api.get("title")
        self.url = data_from_api.get("url")
        self.salary_from = data_from_api.get("salary_from")
        self.salary_to = data_from_api.get("salary_to")
        self.average_salary = self.get_average_salary()
        self.currency = self.get_format_currency(data_from_api)
        self.requirement = data_from_api.get("requirement")

        Vacancy.vacancies_objs_lst.append(self)

    def __repr__(self):
        """
        Возвращает строковое представление объекта Vacancy.
        """
        return (f"{__class__.__name__}(keyword={self.keyword}, title={self.title}, url={self.url},"
                f"salary_from={self.salary_from}, salary_to={self.salary_to}, average_salary={self.average_salary},"
                f"currency={self.currency}, requirement={self.requirement})")

    def get_overview(self):
        """
        Выводит обзор вакансии на экран.
        """
        print()
        print(f"Название - {self.title}")
        print(f"Ссылка - {self.url}")
        print(f"Средняя зарплата - {self.average_salary} {self.currency}")
        print(f"Краткая аннотация - '{self.slice_string(self.requirement, 11)} ...'")

    def get_average_salary(self):
        """
        Вычисляет среднюю зарплату на основе указанных значений salary_from и salary_to.

        Возвращает:
            float: Средняя зарплата.
        """
        if self.salary_from is not None and self.salary_to is not None:
            return round((self.salary_from + self.salary_to) / 2)
        elif self.salary_from is not None:
            return self.salary_from
        elif self.salary_to is not None:
            return self.salary_to
        else:
            return None

    @staticmethod
    def get_format_currency(data_from_api):
        """
        Возвращает отформатированную валюту на основе данных из API.

        Аргументы:
            data_from_api (dict): Словарь с данными о вакансии из API.

        Возвращает:
            str: Отформатированная валюта.
        """
        if data_from_api["currency"] == "RUR" or data_from_api["currency"] == "rub":
            currency_upd = "руб."
            return currency_upd
        else:
            return data_from_api.get("currency")

    @staticmethod
    def slice_string(string, num_spaces):
        """
        Обрезает строку до указанного количества пробелов.

        Аргументы:
            string (str): Исходная строка.
            num_spaces (int): Количество пробелов для обрезки.

        Возвращает:
            str: Обрезанная строка.
        """
        if not string:
            return ""

        count = 0
        result = ""
        for char in string:
            if char == " ":
                count += 1
            if count <= num_spaces:
                result += char
            else:
                break
        return result

    @classmethod
    def get_empty_list(cls):
        """
        Очищает список объектов вакансий.
        """
        cls.vacancies_objs_lst.clear()

    def __eq__(self, other):
        return self.get_average_salary() == other.get_average_salary()

    def __lt__(self, other):
        return self.get_average_salary() < other.get_average_salary()

    def __gt__(self, other):
        return self.get_average_salary() > other.get_average_salary()
