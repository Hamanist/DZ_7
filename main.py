import os

from function.functions import get_student_by_pk, load_students


def main():
    """
    :return: Основной код программы
    """
    user = int(input('Введите номер студента\n'))
    student = get_student_by_pk(user)

    if student is None:
        print('У нас нет такого студента')
    else:
        print(f'Студент {student["full_name"]}\nЗнает {", ".join(student["skills"])}')


    # profession = get_profession_by_title("Frontend")
    # print(profession)

    # user = input('')
    # statistic = check_fitness(student, profession)
    # print(statistic)




main()
