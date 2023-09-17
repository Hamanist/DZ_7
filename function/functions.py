import os
import json

PATH_STUDENTS = os.path.join("..", "data", "students.json")
PATH_PROFESSION = os.path.join("..", "data", "professions.json")


def load_students(path):
    with open(path, encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def load_professions(path):
    with open(path, encoding="utf-8") as file:
        file_json = json.loads(file.read())
        return file_json


def get_student_by_pk(pk):
    for student in load_students(PATH_STUDENTS):
        if student['pk'] == pk:
            return student
    return None


def get_profession_by_title(title):
    for profession in load_professions(PATH_PROFESSION):
        if profession['title'] == title:
            return profession
    return None


def check_fitness(student, profession): ...


print(get_student_by_pk(2))
print(get_profession_by_title('Backend'))
