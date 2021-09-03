def dist(lst,n):
    if len(lst)==0:
        return []
    else:
        return [(lst[0],n)] + dist(lst[1:],n)
print(dist([1,2,3],4))