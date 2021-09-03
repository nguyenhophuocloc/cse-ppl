def powGen(n):
    def inner(h):
        return h**n
    return inner

square = powGen(2)
print(square(4))
