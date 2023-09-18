import os
import json

PATH_STUDENTS = os.path.join("..", "data", "students.json")
PATH_PROFESSION = os.path.join("..", "data", "professions.json")


def load_students(path):
    """
    :param path: принимает путь до файла json
    :return:  Функция загружает список студентов из файла
    """
    with open(path, encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def load_professions(path):
    """
    :param path: принимает путь до файла json
    :return: Функция загружает список профессий из файла
    """
    with open(path, encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def get_student_by_pk(pk):
    """
    :param pk: принимает номер pk
    :return: Функция возвращает словарь с данными студента по его pk
    """
    for student in load_students(PATH_STUDENTS):
        if student['pk'] == pk:
            return student
    return None


def get_profession_by_title(title):
    """
    :param title: принимает название профессии по 'title'
    :return: Функция возвращает словарь с данными профессии по его 'title'
    """
    for profession in load_professions(PATH_PROFESSION):
        if profession['title'] == title:
            return profession
    return None


def check_fitness(student, profession):
    """
    :param student: принимает "skills" студента
    :param profession: принимает "skills" профессии
    :return: возвращает кортеж с данными
    скилы которые знает и не знает + пригодность в процентах
    """
    stud_skills = set(student["skills"])            # преобразуем во множество для
    prof_skills = set(profession["skills"])         # уникальности значений

    knows_the_skills = stud_skills.intersection(prof_skills)
    no_know_the_skills = prof_skills ^ stud_skills
    suitability = int(len(knows_the_skills) / len(prof_skills) * 100)
    return knows_the_skills, no_know_the_skills, suitability
