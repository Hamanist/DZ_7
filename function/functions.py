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


def check_fitness(student, profession):
    stud_skills = set(student["skills"])
    prof_skills = set(profession["skills"])

    knows_the_skills = stud_skills.intersection(prof_skills)
    no_know_the_skills = prof_skills ^ stud_skills
    suitability = int(len(knows_the_skills) / len(prof_skills) * 100)
    return knows_the_skills, no_know_the_skills, suitability


student = get_student_by_pk(1)
profession = get_profession_by_title("Backend")
# print(get_student_by_pk(2))
# print(get_profession_by_title('Backend'))
print(check_fitness(student, profession))
