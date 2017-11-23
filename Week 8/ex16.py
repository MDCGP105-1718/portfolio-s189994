class Fraction(object):
    def __init__ (self,num,denom):
            self.num = num;
            self.denom = denom;

    def _add_(self,other):
        return Fraction (self.num + other.denom)

    def _sub_(self, other):
        return Fraction(self.num - other.denom)

    def _mul_(self, other):
        return Fraction (self.num * other.denom)

    def _div_(self, other):
        return Fraction (self.num / other.denom)

    def inverse(self):
        # self.num , self.denom = self.denom, self.num
            return Fraction (self.denom, self.num)

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)

frac = Fraction(3, 4)
print(frac)
