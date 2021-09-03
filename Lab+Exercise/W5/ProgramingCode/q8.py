from functools import reduce
def flatten(lst):
    return reduce(lambda x,y: x+y,lst,[])

print(flatten([[1,2,3],[4,5],[6,7]]))
