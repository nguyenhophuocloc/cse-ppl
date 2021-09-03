def powGen(x):
    def inner(y):
        return x**y
    return inner
square = powGen(2)
print(square(4))