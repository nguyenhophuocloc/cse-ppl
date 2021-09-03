def flatten(lst):
    if len(lst)==0:
        return []
    else:
        return lst[0] + flatten(lst[1:])


print(flatten([[1,2,3],[4,5],[6,7]]))
#print(len([[1,2,3],[4,5],[6,7]]))