from function.functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    """
    :return: Основной код программы
             student -> выводит полное имя и скилы
             profession -> принимает профессию, после чего проводит анализ на пригодность

    """
    user = int(input('Введите номер студента\n'))
    student = get_student_by_pk(user)

    if student is None:
        print('У нас нет такого студента')
        quit()
    else:
        print(f'Студент {student["full_name"]}\nЗнает {", ".join(student["skills"])}')

    user = input(f'Выберите специальность для оценки студента {student["full_name"]}\n').capitalize()
    profession = get_profession_by_title(user)

    knows_the_skills, no_know_the_skills, suitability = check_fitness(student, profession)
    if profession is None:
        print('Нет такой профессии')
        quit()
    else:
        if knows_the_skills == set():
            knows_the_skills = "абсолютно ни чего по этой профессии"
        print(f'Пригодность {suitability}%')
        print(f'{student["full_name"]} знает {", ".join(knows_the_skills)}')
        print(f'{student["full_name"]} не знает {", ".join(no_know_the_skills)}')


if __name__ == '__main__':
    main()
