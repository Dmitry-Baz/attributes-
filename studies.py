class Lecturer:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # атрибут для хранения оценок по курсам

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def __str__(self):
        return f'Лектор: {self.name}, Оценки: {self.grades}'


class Student:
    def __init__(self, name):
        self.name = name

    def give_grade_to_lecturer(self, lecturer, course, grade):
        # Проверка, что оценка в допустимом диапазоне
        if 0 <= grade <= 10:
            # Проверяем, что лектор закреплен за курсом
            if course in lecturer.grades:
                lecturer.add_grade(course, grade)
                print(f'{self.name} выставил(а) оценку {grade} лектору {lecturer.name} по курсу {course}.')
            else:
                print(f'Лектор {lecturer.name} не закреплен за курсом {course}.')
        else:
            print('Оценка должна быть в диапазоне от 0 до 10.')


# Пример использования
lecturer = Lecturer("Иванов И.И.")
student = Student("Петров П.П.")

# Лектору добавляем курс
lecturer.add_grade("Математика", [])

# Студент выставляет оценку лектору
student.give_grade_to_lecturer(lecturer, "Математика", 8)

# Вывод информации о лекторе
print(lecturer)