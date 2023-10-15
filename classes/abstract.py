from abc import ABC, abstractmethod


class GetByApi(ABC):
    """
    Абстрактный класс для получения вакансий с сервисов
    с использованием их API.

    Метод:
       get_vacancies - абстрактный метод; должен быть реализован в дочерних классах.
    """

    @abstractmethod
    def get_vacancies(self, keyword, num_vacancies):
        """
        Получить вакансии с сервиса по ключевому слову и количеству.

        Аргументы:
            keyword (str) - Поисковый запрос
            num_vacancies (int) - Количество вакансий
        """
        pass


class Saver(ABC):
    """
    Абстрактный класс для сохранения информации о вакансиях

    Метод:
      save_to_file - абстрактный метод; должен быть реализован в дочерних классах.
    """

    @abstractmethod
    def save_to_file(self, vacancies, filename):
        """
        Сохранить данные о вакансиях в файл.

        Аргументы:
           vacancies (list) - Список объектов вакансий
           filename (str) - Имя файла для сохранения
        """
        pass
