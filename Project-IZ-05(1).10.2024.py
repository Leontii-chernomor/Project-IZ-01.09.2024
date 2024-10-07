import string
import keyword


def is_valid_variable_name(var_name):
    if var_name in keyword.kwlist:
        return False
    if var_name.count('_') > 1:
        return False
    if var_name[0].isdigit():
        return False
    allowed_chars = string.ascii_lowercase + string.digits + '_'
    for char in var_name:
        if char not in allowed_chars:
            return False
    return True
user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(user_input))