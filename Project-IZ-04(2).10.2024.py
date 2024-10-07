def even_index_sum_and_multiply(some_list):
    if not some_list:
        return 0
    sum_even_index = sum(some_list[i] for i in range(0, len(some_list), 2))
    return sum_even_index * some_list[-1]
some_list = [5, 8, 24, 8, 11]
result = even_index_sum_and_multiply(some_list)
print(result)