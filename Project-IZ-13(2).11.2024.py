class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Початкове значення повинно бути в межах мінімуму та максимуму.")
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value  # Коригуємо current, якщо він перевищує новий максимум

    def set_min(self, min_min):
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value  # Коригуємо current, якщо він менше нового мінімуму

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Достигнут мінімум")
        self.current -= 1

    def get_current(self):
        return self.current


# Перевірка функціональності
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут мінімум
assert counter.get_current() == 7, 'Test4'