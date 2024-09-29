def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Помилка: ділення на нуль!"
    else:
        return "Невідома операція!"


# Основна програма
while True:
    try:
        # Запитуємо в користувача числа
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть математичну дію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        # Викликаємо функцію для обчислення та виведення результату
        result = calculate(num1, num2, operator)
        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введено неправильне число!")

    # Запитуємо, чи хоче користувач продовжити
    continue_calc = input("Хочете продовжити? (так/ні): ").lower()
    if continue_calc != 'так':
        print("Програма завершена.")
        break