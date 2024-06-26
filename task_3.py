# Helper classes
class PersonalInfo:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender


class MathMethods:
    def average(self, grades: list):
        # Check if the lecturer has grades
        if len(list(grades)):
            # I combine student grades for different courses
            merged_list = [el for lists in list(grades) for el in lists]
            # Finding the average and rounding the value to one decimal place
            return round(sum(merged_list) / len(merged_list), 1)
        else:
            return 'Еще нет оценок'


class CompareTwoPeople:
    def compare(self, second):
        lector_info = [
            f'{self.name} {self.surname}',
            f'{second.name} {second.surname}',
            self.average_value,
            second.average_value
        ]
        if lector_info[2] > lector_info[3]:
            text = f'— результативнее {lector_info[1]}. Cредняя оценка за лекции составляет:'
            return f'{lector_info[0]} {text} {lector_info[2]}'
        elif lector_info[2] < lector_info[3]:
            text = f'— результативнее {lector_info[0]}. Cредняя оценка за лекции составляет:'
            return f'{lector_info[1]} {text} {lector_info[3]}'
        else:
            text = (f'{lector_info[0]} и {lector_info[1]} одинаково результативны. Их балл '
                    f'составляет: {lector_info[3]}')
            return f'Лекторы {text}'


# Student's Class
class Student(PersonalInfo, MathMethods, CompareTwoPeople):
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = dict()
        self.average_value: int

    def rate_lecturer(self, lecturer, course, grade):
        """
        :param lecturer: «Lecturer whose work must be evaluated by the student»
        :param course: «Course assigned to the selected lecturer»
        :param grade: «The grade given by the student to the selected lecturer for this course»
        :return: «Completed dictionary attribute for the Lecturer class»
        """
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in
                self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        self.average_value = self.average(list(self.grades.values()))
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        average_rate = f'Средняя оценка за лекции: {self.average_value}'
        courses_in_progress = f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}'
        courses_finished = f'Завершенные курсы: {', '.join(self.finished_courses)}'
        return f'{name}\n{surname}\n{average_rate}\n{courses_in_progress}\n{courses_finished}'


# Parent class
class Mentor(PersonalInfo):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.courses_attached = []


# Lecturers class
class Lecturer(Mentor, MathMethods, CompareTwoPeople):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.grades = dict()
        self.average_value: int

    def __str__(self) -> str:
        self.average_value = self.average(list(self.grades.values()))
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_value}')


# Reviewers class
class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if (isinstance(student, Student) and course in student.courses_in_progress and course in
                self.courses_attached):
            if course in student.grades:
                student.grades[course] += [i for i in grade]
            else:
                student.grades[course] = [i for i in grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Students
evelina_sokolova = Student('Эвелина', 'Соколова', 'Женщина')
sergey_makarov = Student('Сергей', 'Макаров', 'Мужчина')
# Students / Finished courses
evelina_sokolova.finished_courses += ['Вводный модуль', 'Основы Python']
sergey_makarov.finished_courses += ['Вводный модуль', 'Основы Python']
# Students / Courses in progress
evelina_sokolova.courses_in_progress += ['Git', 'Python']
sergey_makarov.courses_in_progress += ['Git', 'Python']

# Reviewers
maxim_reviewer = Reviewer('Максим', 'Романов', 'Мужчина')
garik_reviewer = Reviewer('Гарик', 'Добрый', 'Мужчина')
# Reviewers / Courses in progress
maxim_reviewer.courses_attached += ['Python']
garik_reviewer.courses_attached += ['Git']

# Lecturers
oleg_lecturer = Lecturer('Олег', 'Темнов', 'Мужчина')
dima_lecturer = Lecturer('Дмитрий', 'Окунев', 'Мужчина')
# Lecturers / Courses attached
oleg_lecturer.courses_attached += ['Git', 'Python']
dima_lecturer.courses_attached += ['Python']

# The reviewer gives a grade to the student
# (Each element in the list, which is passed as a grade parameter, represents the grade for a
# single lesson)
garik_reviewer.rate_student(evelina_sokolova, 'Git', [8, 7])
maxim_reviewer.rate_student(evelina_sokolova, 'Python', [10, 10, 8])
garik_reviewer.rate_student(sergey_makarov, 'Git', [6, 8])
maxim_reviewer.rate_student(sergey_makarov, 'Python', [9, 10, 7])

# A student gives a grade to the lecture for a course
sergey_makarov.rate_lecturer(oleg_lecturer, 'Git', 5)
evelina_sokolova.rate_lecturer(oleg_lecturer, 'Python', 10)
evelina_sokolova.rate_lecturer(dima_lecturer, 'Python', 9)
sergey_makarov.rate_lecturer(oleg_lecturer, 'Python', 7)
sergey_makarov.rate_lecturer(dima_lecturer, 'Python', 8)

# Displaying the result of the code on the screen for checking
print('[Student] Evelina Sokolova:', evelina_sokolova.grades)
print('[Student] Sergey Makarov:', sergey_makarov.grades)
print('[Lecturer] Oleg Temnov:', oleg_lecturer.grades)

# Print for 3 Task
print('', '— Reviewer —', maxim_reviewer, sep='\n')
print('', '— 1 Lecturer —', oleg_lecturer, sep='\n')
print('', '— 2 Lecturer —', dima_lecturer, sep='\n')
print('', '— 1 Student —', evelina_sokolova, sep='\n')
print('', '— 2 Student —', sergey_makarov, sep='\n')

print('', 'Задача: Сравнение лекторов и студентов', sep='\n')
print(oleg_lecturer.compare(dima_lecturer))
print(evelina_sokolova.compare(sergey_makarov))
