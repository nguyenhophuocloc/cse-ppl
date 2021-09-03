def lstSquare(n):
    
    if n == 0:
        return []
    else:
        #lst.insert(0,n*n)
        return lstSquare(n-1)+ [n*n] 

print(lstSquare(4))

"""
    lst=[]
    for x in range(1,n):
        lst.append(x*x)
    return lst
"""