

some_list1 = [ 1, 53, 19]
some_list1.insert(0, "7")
print(some_list1)
some_list2 = [5]
print(some_list2)
some_list3 = [ ]
print(some_list3)


def move_last_to_first(input_list):
    if len(input_list) <= 1:
        return input_list
    return [input_list[-1]] + input_list[:-1]

print(move_last_to_first([25, 14, 95, 70]))
print(move_last_to_first([99]))
print(move_last_to_first([]))