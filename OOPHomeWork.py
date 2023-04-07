def _GradesMean(gradesdict):
    allgrades = []
    for course, grades in gradesdict.items():
        for grade in grades:
            allgrades.append(grade)
    if len(allgrades) > 0:
        average = sum(allgrades) / len(allgrades)
        return average
    return 0


def AverageForLecturers(lecturers: list, course):
    allavergrades = []
    for lect in lecturers:
        if not isinstance(lect, Lecturer) and course in lect.courses_attached:
            return 'Ошибка'
        allavergrades.append(_GradesMean(lect.grades))
    res = sum(allavergrades) / len(allavergrades)
    return res


def AverageForStudents(students: list, course):
    allavergrades = []
    for stud in students:
        if not isinstance(stud, Student) and course in stud.courses_in_progress:
            return 'Ошибка'
        allavergrades.append(_GradesMean(stud.grades))
    res = sum(allavergrades) / len(allavergrades)
    return res


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __str__(self):
        average = _GradesMean(self.grades)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        self_average = _GradesMean(self.grades)
        other_average = _GradesMean(other.grades)
        if not isinstance(other, Student):
            return 'Not a Student'
        else:
            return self_average < other_average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average = _GradesMean(self.grades)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}'
        return res

    def __lt__(self, other):
        self_average = _GradesMean(self.grades)
        other_average = _GradesMean(other.grades)
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer'
        else:
            return self_average < other_average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
