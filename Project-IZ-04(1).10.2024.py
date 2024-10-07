def move_zeros_to_end(some_list):
    non_zero_index = 0
    for i in range(len(some_list)):
        if lst[i] != 0:
            lst[non_zero_index], lst[i] = lst[i], lst[non_zero_index]
            non_zero_index += 1
lst = [0, 189, 0, 12, 94, 0]
move_zeros_to_end(lst)
print(lst)