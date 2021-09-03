lst = [5, 7, 12, -4]


def func1(lst):
    return [x*2 for x in lst]


def func2(lst):
    if not lst:
        return []
    else:
        return [lst[0]*2] + func2(lst[1:])


def func3(lst):
    return list(map(lambda x: x*2, lst))


print(func3(lst))
