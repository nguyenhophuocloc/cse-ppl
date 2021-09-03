from functools import reduce
lst = [[1, 2, 3], ['a', 'b', 'c', 'd'], [1.1, 2.1, 3.1]]


def func1(lst):
    o = []
    """
    for i in range(0,len(lst)):
        for j in range(0,len(lst[i])):
            o.append(lst[i][j])
    """

    return [lst[i][j] for i in range(0, len(lst)) for j in range(0, len(lst[i]))]


def func2(lst):
    if len(lst) == 0:
        return []
    else:
        return lst[0] + func2(lst[1:])

def func3(lst):
    return reduce(lambda x,y:x+y,lst,lst[0])
print(func3(lst))
