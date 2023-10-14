from abc import ABC, abstractmethod


class GetByApi(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, num_vacancies):
        pass


class Saver(ABC):
    @abstractmethod
    def save_to_file(self, vacancies, filename):
        pass
