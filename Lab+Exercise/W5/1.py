def compose(f,g):
   def h(x):
      return reduce(lambda x, y: y(x), reversed(g), args)
   return h
   

def square(x):
   return x * x

def increase(x):
   return x + 1

def double(x):
   return x * 2

m=compose(double,increase)
print(m(5)) # Kết quả là 12 do (5 + 1) * 2
m = compose()
print(m(5)) # Kết quả là 52 do (5 * 5 + 1) * 2