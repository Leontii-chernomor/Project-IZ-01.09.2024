class TooManyStudentsException(Exception):
    """Користувацький виняток, що викликається при перевищенні ліміту студентів у групі."""
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)

class Student:
    """Клас для опису студента."""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

class Group:
    """Клас для опису групи студентів."""
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        """Додає студента до групи. Викликає виняток, якщо у групі більше 10 студентів."""
        if len(self.students) >= 10:
            raise TooManyStudentsException()
        self.students.append(student)

    def remove_student(self, student):
        """Видаляє студента з групи."""
        self.students.remove(student)

    def __str__(self):
        student_list = "\n".join(str(student) for student in self.students)
        return f"Група {self.group_name}:\n{student_list}"

# Використання:
try:
    group = Group("ПМ-01")
    # Додаємо 11 студентів
    for i in range(11):
        group.add_student(Student(f"Студент{i+1}", f"Прізвище{i+1}"))
except TooManyStudentsException as e:
    print(f"Виняток: {e}")
finally:
    print(group)