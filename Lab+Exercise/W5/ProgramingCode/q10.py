from functools import reduce
def compose(*arg):
    def inner(n):
        return reduce(lambda x,y: y(x), reversed(arg),n)
    return inner
def square(n):
    return n**2


def increase(n):
    return n+1

def double(n):
    return n*2

f = compose(increase,square,double)
print(f(3))