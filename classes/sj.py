import datetime
import os
import time

import requests

from dotenv import load_dotenv

from classes.abstract import GetByApi

load_dotenv()


class SuperJob(GetByApi):
    def get_vacancies(self, keyword, num_vacancies=25):
        """
        Получить список вакансий из API SuperJob на основе указанного ключевого слова.

        Аргументы:
            keyword (str): Ключевое слово для поиска вакансий.
            num_vacancies (int, optional): Количество вакансий для получения.

        Возвращает:
            list: Список словарей, представляющих полученные вакансии.
        """
        __api_key = os.getenv("SJ_TOKEN")
        __URL = "https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": __api_key}
        search_from = datetime.datetime.now() - datetime.timedelta(days=30)
        unix_time = int(time.mktime(search_from.timetuple()))
        per_page = 20
        page = 1
        all_vacancies = []

        while len(all_vacancies) < num_vacancies:
            params = {
                "keyword": keyword,
                "per_page": per_page,
                "page": page,
                "town": "Москва",
                "currency": "rub",
                "date_published_from": unix_time,
            }

            # Проверка соединения с API
            check = requests.get(url=__URL, headers=headers)
            if check.status_code != requests.codes.ok:
                print(f"{check.status_code} - ошибка соединения. Программа завершается.")
                exit()

            response = requests.get(url=__URL, headers=headers, params=params).json()

            if "objects" not in response or not response["objects"]:
                # Если нет вакансий по запросу, выходим из цикла
                break

            result = []
            for item in response["objects"]:
                requirement = item.get("candidat", None)
                if requirement is not None:
                    requirement = requirement.strip().replace("\n•", "").replace("\n", "").replace("\n\n", "")
                tmp = {
                    "keyword": keyword.upper(),
                    "id": item.get("id", None),
                    "title": item.get("profession", None),
                    "url": item.get("link", None),
                    "salary_from": item.get("payment_from", None),
                    "salary_to": item.get("payment_to", None),
                    "currency": item.get("currency", None),
                    "requirement": requirement,
                }
                result.append(tmp)

            all_vacancies.extend(result)
            page += 1

            if len(response["objects"]) < per_page:
                break

        return all_vacancies[:num_vacancies]
