def lessThan1(n, lst):
    return [x for x in lst if x < n]


def lessThan2(n, lst):
    if len(lst)==0:
        return []
    else:
        if(lst[0] < n):
            return [lst[0]] + lessThan2(n,lst[1:])
        else:
            return lessThan2(n,lst[1:])

def lessThan3(n,lst):
    return list(filter(lambda x: x<n,lst))
print(lessThan3(50, [1, 55, 6, 2]))
