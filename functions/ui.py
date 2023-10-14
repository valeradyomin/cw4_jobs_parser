from classes.hh import HeadHunter
from classes.saver import JsonOut
from classes.vacancy import Vacancy


def user_interaction():
    while True:
        Vacancy.get_empty_list()
        print("\nНачальное меню:")
        interaction = input("укажите действие:\n1 - HH\n2 - SJ\n3 - Выход\n")
        if interaction == "1":
            while True:
                keyword = input("укажите ключевое слово вакансии:\n").strip()
                if keyword == "3":
                    break
                while True:
                    try:
                        num_vacancies = int(input("укажите количество вакансий:\n"))
                        break
                    except ValueError:
                        print("Введено некорректное значение. Пожалуйста, введите число.")
                hh_by_api = HeadHunter()
                hh_data_from_api = hh_by_api.get_vacancies(keyword, num_vacancies)
                if not hh_data_from_api:
                    print(f"Для ключевого слова '{keyword}' не найдено вакансий.")
                else:
                    for data in hh_data_from_api:
                        Vacancy(data)

                    vacancies = Vacancy.vacancies_objs_lst
                    json_saver = JsonOut(vacancies)

                    print("\nМеню отображения результатов:")
                    sub_interaction = input("отобразить результат:\n1 - полный"
                                            "\n2 - отсортированный\n3 - средняя зарплата от"
                                            "\n4 - ТОП-№ вакансий\n")

                    if sub_interaction == "1":
                        json_saver.save_to_file(vacancies, filename="01.json")
                        for vacancy in vacancies:
                            vacancy.get_overview()
                        print(f"Сохранено в файл {len(vacancies)} вакансий")
                        break

                    elif sub_interaction == "2":
                        sorted_vacancies = json_saver.get_sort_by_average_salary(filename="02.json")
                        for vacancy in sorted_vacancies:
                            vacancy.get_overview()
                        print(f"Сохранено в файл {len(sorted_vacancies)} вакансий")
                        break

                    elif sub_interaction == "3":
                        while True:
                            while True:
                                try:
                                    min_salary = int(input("Укажите величину минимальной средней зарплаты: "))
                                    break
                                except ValueError:
                                    print("Введено некорректное значение. Пожалуйста, введите число.")
                            filtered_vacancies = [vacancy for vacancy in vacancies if
                                                  vacancy.average_salary >= min_salary]
                            if len(filtered_vacancies) > 0:
                                vacancies_by_average_salary = json_saver.get_vacancies_by_average_salary(min_salary,
                                                                                                         filename="03.json")
                                for vacancy in vacancies_by_average_salary:
                                    vacancy.get_overview()
                                print(f"Сохранено в файл {len(vacancies_by_average_salary)} вакансий")
                                break
                            else:
                                print(
                                    "Нет вакансий с указанной минимальной зарплатой.")
                        break

                    elif sub_interaction == "4":
                        while True:
                            try:
                                top_n = int(input("Укажите количество топ-вакансий по зарплате\n"))
                                if top_n <= num_vacancies:
                                    top_n_vacancies = json_saver.get_top_n_vacancies(top_n, filename="04.json")
                                    for vacancy in top_n_vacancies:
                                        vacancy.get_overview()
                                    print(f"Сохранено в файл {len(top_n_vacancies)} вакансий")
                                    break
                                else:
                                    print(f"Укажите значение меньше {num_vacancies} либо равно")
                            except ValueError:
                                print("Введено некорректное значение.")
                        break

        elif interaction == "2":
            pass
        elif interaction == "3":
            exit()
