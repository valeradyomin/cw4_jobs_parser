import json
import os

from classes.abstract import Saver
from classes.vacancy import Vacancy


class JsonOut(Saver):
    def __init__(self, vacancies):
        self.vacancies = vacancies
        self.data_folder = "./_resulting_data"

    @staticmethod
    def vacancy_serializer(obj):
        if isinstance(obj, Vacancy):
            return obj.__dict__
        raise TypeError("Объект типа 'Vacancy' не может быть сериализован в JSON")

    def save_to_file(self, vacancies, filename):
        file_path = os.path.join(self.data_folder, filename)
        with open(file_path, 'w') as file:
            json.dump(vacancies, file, indent=4, default=self.vacancy_serializer, ensure_ascii=False)

    def get_vacancies_by_average_salary(self, min_salary, filename):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if vacancy.average_salary >= min_salary]
        self.save_to_file(filtered_vacancies, filename)
        return filtered_vacancies

    def get_sort_by_average_salary(self, filename):
        sorted_vacancies = sorted(self.vacancies, key=lambda vacancy: vacancy.average_salary, reverse=True)
        self.save_to_file(sorted_vacancies, filename)
        return sorted_vacancies

    def get_top_n_vacancies(self, top_n, filename):
        sorted_vacancies = sorted(self.vacancies, key=lambda vacancy: vacancy.average_salary, reverse=True)
        top_n_vacancies = sorted_vacancies[:top_n]
        self.save_to_file(top_n_vacancies, filename)
        return top_n_vacancies
