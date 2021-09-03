class Rational:

    def __init__(self, n=0, d=1):
        if d != 0:
            self.n = n
            self.d = d
            __g = gcd(n, d)
            self.numer = n/self.__g
            self.denom = d/self.__g
        else:
            raise SystemExit("d==0")

    def __gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.__gcd(b, a % b)

    def __add(self, that):
        if isinstance(that, Rational):
            return Rational(self.numer*that.denom+that.numer*denom,
                            self.denom*that.denom)
        elif isinstance(that, int):
            return self + Rational(that)
        else:
            return None

    def __toString(self):
        return str(self.numer) + "/" + str(self.denom)
