def lstSquare(n):
    if n==0:
        return []
    else:
        return lstSquare(n-1)+[n*n]

print(lstSquare(3))