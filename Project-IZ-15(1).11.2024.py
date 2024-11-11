import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Обчислює площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Перевизначення оператора == для порівняння площ прямокутників."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """Перевизначення оператора + для складання площ прямокутників."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.get_square() + other.get_square()
        return Rectangle.from_area(new_area)

    def __mul__(self, n):
        """Перевизначення оператора * для множення площі прямокутника на число."""
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        return Rectangle.from_area(new_area)

    def __str__(self):
        """Повертає рядкове представлення прямокутника."""
        return f"Rectangle(width={self.width}, height={self.height})"

    @staticmethod
    def from_area(area):
        """Створює прямокутник із заданою площею, підбираючи сторони."""
        side = math.sqrt(area)
        width = math.floor(side)
        height = math.ceil(area / width)
        # Перевірка на точну відповідність площі
        if width * height != area:
            width = math.gcd(int(area), width)
            height = area // width
        return Rectangle(width, height)


# Тести
if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)

    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    assert r3.get_square() == 26, 'Test3'

    r4 = r1 * 4
    assert r4.get_square() == 32, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

    print("Всі тести пройдено успішно!")