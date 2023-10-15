from classes.hh import HeadHunter
from classes.sj import SuperJob
from classes.saver import JsonOut
from classes.vacancy import Vacancy


def user_interaction():
    """
    Функция взаимодействия с пользователем. Получает запросы и выводит результат на экран, сохраняет в файл.
    """
    interaction_count = 0
    while True:
        Vacancy.get_empty_list()
        interaction_count += 1
        print("\nНачальное меню программы по поиску работы на платформах предоставления вакансий:")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        interaction = input("Укажите действие:"
                            "\n1 - использовать HeadHunter\n2 - использовать SuperJob\n3 - Выход\n")
        if interaction == "1":
            while True:
                keyword = input("Укажите ключевое слово вакансии:\n").strip()
                if keyword == "3":
                    break
                while True:
                    try:
                        num_vacancies = int(input("Укажите количество вакансий:\n"))
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
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    sub_interaction = input("Отобразить и сохранить в файл результат:\n1 - полная выборка"
                                            "\n2 - отсортированный по убыванию зарплаты (сначала большая зарплата)"
                                            "\n3 - с зарплатой больше указанного значения (указать минимальную)"
                                            "\n4 - ТОП-№ вакансий по зарплате (указать количество выборки)\n")

                    if sub_interaction == "1" and sub_interaction in ("1", "2", "3", "4"):
                        json_saver.save_to_file(
                            vacancies, filename=f"{interaction_count}_{HeadHunter.__name__}_{keyword}_full.json"
                        )
                        for vacancy in vacancies:
                            vacancy.get_overview()
                        print(f"\n-----------> Сохранено в файл {len(vacancies)} вакансий")
                        break

                    elif sub_interaction == "2" and sub_interaction in ("1", "2", "3", "4"):
                        sorted_vacancies = json_saver.get_sort_by_average_salary(
                            filename=f"{interaction_count}_{HeadHunter.__name__}_{keyword}_sorted.json"
                        )
                        for vacancy in sorted_vacancies:
                            vacancy.get_overview()
                        print(f"\n-----------> Сохранено в файл {len(sorted_vacancies)} вакансий")
                        break

                    elif sub_interaction == "3" and sub_interaction in ("1", "2", "3", "4"):
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
                                vacancies_by_average_salary = json_saver.get_vacancies_by_average_salary(
                                    min_salary,
                                    filename=f"{interaction_count}_{HeadHunter.__name__}_{keyword}_average.json"
                                )
                                for vacancy in vacancies_by_average_salary:
                                    vacancy.get_overview()
                                print(f"\n-----------> Сохранено в файл {len(vacancies_by_average_salary)} вакансий")
                                break
                            else:
                                print(
                                    "Нет вакансий с указанной минимальной зарплатой. Введите другое значение.")
                        break

                    elif sub_interaction == "4" and sub_interaction in ("1", "2", "3", "4"):
                        while True:
                            try:
                                top_n = int(input("Укажите количество топ-вакансий по зарплате\n"))
                                if top_n <= num_vacancies:
                                    top_n_vacancies = json_saver.get_top_n_vacancies(
                                        top_n, filename=f"{interaction_count}_{HeadHunter.__name__}_{keyword}_top.json"
                                    )
                                    for vacancy in top_n_vacancies:
                                        vacancy.get_overview()
                                    print(f"\n-----------> Сохранено в файл {len(top_n_vacancies)} вакансий")
                                    break
                                else:
                                    print(f"Укажите значение меньше {num_vacancies} либо равно")
                            except ValueError:
                                print("Введено некорректное значение. Пожалуйста, введите число.")
                        break
                    else:
                        Vacancy.get_empty_list()
                        print("Некорректный ввод. Повторите действие.")

        elif interaction == "2":
            while True:
                keyword = input("Укажите ключевое слово вакансии:\n").strip()
                if keyword == "3":
                    break
                while True:
                    try:
                        num_vacancies = int(input("Укажите количество вакансий:\n"))
                        break
                    except ValueError:
                        print("Введено некорректное значение. Пожалуйста, введите число.")
                sj_by_api = SuperJob()
                sj_data_from_api = sj_by_api.get_vacancies(keyword, num_vacancies)
                if not sj_data_from_api:
                    print(f"Для ключевого слова '{keyword}' не найдено вакансий.")
                else:
                    for data in sj_data_from_api:
                        Vacancy(data)

                    vacancies = Vacancy.vacancies_objs_lst
                    json_saver = JsonOut(vacancies)

                    print("\nМеню отображения результатов:")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    sub_interaction = input("Отобразить и сохранить в файл результат:\n1 - полная выборка"
                                            "\n2 - отсортированный по убыванию зарплаты (сначала большая зарплата)"
                                            "\n3 - с зарплатой больше указанного значения (указать минимальную)"
                                            "\n4 - ТОП-№ вакансий по зарплате (указать количество выборки)\n")

                    if sub_interaction == "1" and sub_interaction in ("1", "2", "3", "4"):
                        json_saver.save_to_file(
                            vacancies, filename=f"{interaction_count}_{SuperJob.__name__}_{keyword}_full.json"
                        )
                        for vacancy in vacancies:
                            vacancy.get_overview()
                        print(f"\n-----------> Сохранено в файл {len(vacancies)} вакансий")
                        break

                    elif sub_interaction == "2" and sub_interaction in ("1", "2", "3", "4"):
                        sorted_vacancies = json_saver.get_sort_by_average_salary(
                            filename=f"{interaction_count}_{SuperJob.__name__}_{keyword}_sorted.json"
                        )
                        for vacancy in sorted_vacancies:
                            vacancy.get_overview()
                        print(f"\n-----------> Сохранено в файл {len(sorted_vacancies)} вакансий")
                        break

                    elif sub_interaction == "3" and sub_interaction in ("1", "2", "3", "4"):
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
                                vacancies_by_average_salary = json_saver.get_vacancies_by_average_salary(
                                    min_salary,
                                    filename=f"{interaction_count}_{SuperJob.__name__}_{keyword}_average.json"
                                )
                                for vacancy in vacancies_by_average_salary:
                                    vacancy.get_overview()
                                print(f"\n-----------> Сохранено в файл {len(vacancies_by_average_salary)} вакансий")
                                break
                            else:
                                print(
                                    "Нет вакансий с указанной минимальной зарплатой. Введите другое значение.")
                        break

                    elif sub_interaction == "4" and sub_interaction in ("1", "2", "3", "4"):
                        while True:
                            try:
                                top_n = int(input("Укажите количество топ-вакансий по зарплате\n"))
                                if top_n <= num_vacancies:
                                    top_n_vacancies = json_saver.get_top_n_vacancies(
                                        top_n, filename=f"{interaction_count}_{SuperJob.__name__}_{keyword}_top.json"
                                    )
                                    for vacancy in top_n_vacancies:
                                        vacancy.get_overview()
                                    print(f"\n-----------> Сохранено в файл {len(top_n_vacancies)} вакансий")
                                    break
                                else:
                                    print(f"Укажите значение меньше {num_vacancies} либо равно")
                            except ValueError:
                                print("Введено некорректное значение. Пожалуйста, введите число.")
                        break
                    else:
                        Vacancy.get_empty_list()
                        print("Некорректный ввод. Повторите действие.")
        elif interaction == "3":
            exit()
