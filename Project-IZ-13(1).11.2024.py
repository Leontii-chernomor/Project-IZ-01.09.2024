class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, запис у журналі: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Група: {self.number}\nСтуденти:\n{all_students}"


# Тестування класів
st1 = Student('Чоловік', 30, 'Стив', 'Джобс', 'AN142')
st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)
# Група: PD1
# Студенти:
# Стив Джобс, 30 років, Чоловік, запис у журналі: AN142
# Ліза Тейлор, 25 років, Жінка, запис у журналі: AN145

assert str(gr.find_student('Джобс')) == str(st1), 'Test1'
assert gr.find_student('Тейлор') is not None, 'Test2'
assert gr.find_student('Тейлор') == st2, 'Test3'
assert gr.find_student('Jobs2') is None, 'Test4'
assert isinstance(gr.find_student('Джобс'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Тейлор')
print(gr)  # Тільки один студент
"""
Група: PD1
Студенти:
Стив Джобс, 30 років, Чоловік, запис у журналі: AN142
"""

gr.delete_student('Тейлор')  # Немає помилки!