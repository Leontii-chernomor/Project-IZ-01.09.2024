def convert_seconds(seconds):

    days, remaining_seconds = divmod(seconds, 24 * 60 * 60)  # 1 день = 86400 секунд
    hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)  # 1 година = 3600 секунд
    minutes, remaining_seconds = divmod(remaining_seconds, 60)  # 1 хвилина = 60 секунд
    secs = remaining_seconds

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    time_string = f"{days} {day_word}, {hours:02}:{minutes:02}:{secs:02}"

    return time_string

user_input = int(input("Введіть кількість секунд (0-8640000): "))
if 0 <= user_input < 8640000:
    result = convert_seconds(user_input)
    print(result)
else:
    print("Число має бути в межах від 0 до 8640000.")