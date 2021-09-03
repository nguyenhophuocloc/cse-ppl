from functools import reduce
def increase(n): return n+1
def square(n): return n**2
def compose(*g):
    def h(n):
        return reduce(lambda x,y: y(x), reversed(g),n)
    return h

f = compose(increase,square)
print(f(3)) #increase(square(3)) = 10