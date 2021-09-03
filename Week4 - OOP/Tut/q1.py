"""
class Type:
    def __repr__(cls):
        return cls.__name__


class O(object, metaclass=Type):
    pass
"""

class O:
    def process(self):
        print("Hello mro")
class A(O):
    pass


class B(O):
    pass


class C(O):
    pass


class D(A, B):
    pass


class E(C, A):
    pass


class F(D, E, B):
    pass


print(F.mro())
"""
class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()  
obj.process()    
print(C.mro())   # print MRO for class C
"""