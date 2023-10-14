from classes.abstract import Saver


class JsonOut(Saver):
    def __init__(self, vacancies):
        self.vacancies = vacancies
        self.data_folder = "./_resulting_data"
