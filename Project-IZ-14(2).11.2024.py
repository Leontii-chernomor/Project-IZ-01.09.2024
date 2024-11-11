class TooManyStudentsException(Exception):
    """Користувацький виняток, що викликається при перевищенні ліміту студентів у групі."""

    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)


# student.py
class Student:
    """Клас для опису студента."""

    def __init__(self, gender, age, name, surname, student_id):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __eq__(self, other):
        """Порівняння студентів за рядковим представленням."""
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        """Забезпечує хешування студента."""
        return hash(str(self))


# group.py
class Group:
    """Клас для опису групи студентів."""

    def __init__(self, group_name):
        self.group_name = group_name
        self.students = set()  # Використовуємо множину для унікальних студентів

    def add_student(self, student):
        """Додає студента до групи. Викликає виняток, якщо у групі більше 10 студентів."""
        if len(self.students) >= 10:
            raise TooManyStudentsException()
        self.students.add(student)

    def remove_student(self, surname):
        """Видаляє студента з групи за прізвищем."""
        student = self.find_student(surname)
        if student:
            self.students.remove(student)

    def find_student(self, surname):
        """Знаходить студента за прізвищем."""
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def __str__(self):
        student_list = "\n".join(str(student) for student in self.students)
        return f"Група {self.group_name}:\n{student_list}"


# main.py
def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')

    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)

    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Jobs2') is None

    gr.remove_student('Taylor')
    print(gr)  # Only one student remains


if __name__ == "__main__":
    main()