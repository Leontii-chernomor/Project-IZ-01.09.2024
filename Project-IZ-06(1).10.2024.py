import string
def letters_between(input_string):
    start_letter, end_letter = input_string.split('-')
    start_index = string.ascii_letters.index(start_letter)
    end_index = string.ascii_letters.index(end_letter)
    return string.ascii_letters[start_index:end_index + 1]
user_input = input("Введіть дві літери через дефіс (наприклад, a-e): ")
result = letters_between(user_input)
print(result)