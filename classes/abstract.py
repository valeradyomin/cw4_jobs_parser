from abc import ABC, abstractmethod


class GetByApi(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, num_vacancies):
        pass
