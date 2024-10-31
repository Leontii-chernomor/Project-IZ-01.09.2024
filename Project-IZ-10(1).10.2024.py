def some_gen(begin, end, func):
    """
    begin: початковий елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує наступне значення для послідовності
    """
    current_value = begin

    for _ in range(end):
        yield current_value
        current_value = func(current_value)


def pow(x):
    return x ** 2


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')