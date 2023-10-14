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