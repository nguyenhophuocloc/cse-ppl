from functools import reduce


def compose1(*g):
    cps = compose1(*g[:-1]) if len(g) > 2 else g[-2]
    return lambda num: cps(g[-1](num))


def compose2(*g):
    def h(args):
        return reduce(lambda x, y: y(x), reversed(g), args)
    return h


def compose(*g):
    def h(args):
        for x in reversed(g):
            args = x(args)
        return args
    return h


def double(x):
    return x*2


def increase(x):
    return x+1


def square(x):
    return x*x


m = compose1(square, increase, double)
print(m(5))
