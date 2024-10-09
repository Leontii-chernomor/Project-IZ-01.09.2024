def multiply_digits_until_single_digit(number):
    while number > 9:
        product = 1
        while number > 0:
            digit = number % 10
            product *= digit
            number //= 10
        number = product
    return number

user_input = int(input("Введіть ціле число: "))
result = multiply_digits_until_single_digit(user_input)
print("Результат:", result)