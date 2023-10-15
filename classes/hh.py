import requests

from classes.abstract import GetByApi


class HeadHunter(GetByApi):
    def get_vacancies(self, keyword, num_vacancies=25):
        __URL = "https://api.hh.ru/vacancies"
        headers = {'User-Agent': 'api-test-agent'}
        params = {"text": keyword,
                  "per_page": num_vacancies,
                  "area": 1,
                  "only_with_salary": True,
                  "currency": "RUR",
                  }
        response = requests.get(url=__URL, headers=headers, params=params).json()

        check = requests.get("https://api.hh.ru/vacancies")
        if check.status_code != requests.codes.ok:
            print(f"{check.status_code} - ошибка соединения. Программа завершается.")
            exit()

        if "items" not in response or not response["items"]:
            # print(f"К сожалению нет вакансий по запросу: {keyword}")
            return []

        result = []
        for item in response["items"]:
            salary = item.get("salary", None)
            requirement = item.get("snippet", {}).get("requirement", None)
            if requirement is not None:
                requirement = requirement.replace("<highlighttext>", "").replace("</highlighttext>", "")
            tmp = {
                "keyword": keyword.upper(),
                "id": item.get("id", None),
                "title": item.get("name", None),
                "url": item.get("alternate_url", None),
                "salary_from": salary.get("from") if salary and "from" in salary else None,
                "salary_to": salary.get("to") if salary and "to" in salary else None,
                "currency": salary.get("currency") if salary and "currency" in salary else None,
                "requirement": requirement,
            }
            result.append(tmp)

        return result
