from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю.")
        self.original_a = a  # Початковий чисельник
        self.original_b = b  # Початковий знаменник
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        """Скорочує дріб до найпростішого вигляду."""
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    def __mul__(self, other):
        """Множення дробів."""
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        """Додавання дробів."""
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Віднімання дробів."""
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Порівняння дробів на рівність."""
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        """Менше ніж."""
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        """Більше ніж."""
        return self.a * other.b > other.a * self.b

    def __str__(self):
        """Повертає несокращену форму дробу."""
        return f"Fraction: {self.original_a}, {self.original_b}"

# Тести
if __name__ == "__main__":
    f_a = Fraction(2, 3)
    f_b = Fraction(3, 6)

    f_c = f_b + f_a
    assert str(f_c) == 'Fraction: 21, 18'  # Нескорочений вигляд

    f_d = f_b * f_a
    assert str(f_d) == 'Fraction: 6, 18'

    f_e = f_a - f_b
    assert str(f_e) == 'Fraction: 3, 18'

    assert f_d < f_c  # True
    assert f_d > f_e  # True
    assert f_a != f_b  # True

    f_1 = Fraction(2, 4)
    f_2 = Fraction(3, 6)
    assert f_1 == f_2  # True

    print('OK')