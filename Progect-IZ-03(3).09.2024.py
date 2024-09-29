def split_list(some_list):
    if len(some_list) == 0:
        return [[], []]

    middle_index = (len(some_list) + 1) // 2

    first_part = some_list[:middle_index]
    second_part = some_list[middle_index:]

    return [first_part, second_part]

print(split_list([85, 1, 99, 5748]))
print(split_list([89, 723, 48, 321, 1]))
print(split_list([]))