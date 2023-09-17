from function.functions import get_student_by_pk, get_profession_by_title
def main():
    """
    :return: Основной код программы
    """
    # user = input('Введите номер студента\n')
    student = get_student_by_pk(1)
    print(student)
    # if student is None:
    #     print('У нас нет такого студента')

    profession = get_profession_by_title("Frontend")
    print(profession)


if __name__ == '__main__':
    print(main())
