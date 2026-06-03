from algorithms import gcd
class Rational:

    def __init__(self, *args):

        if len(args) == 1:
            inputString = args[0]

            if inputString.isnumeric():
                self.num = int(inputString)
                self.den = 1
                return

            slashPosition = inputString.find("/")

            self.num = int(inputString[:slashPosition])
            self.den = int(inputString[slashPosition + 1:])

        elif len(args) == 2:
            num, den = args

            assert den != 0

            self.num = num
            self.den = den

        else:
            raise TypeError("Expected either 1 or 2 arguments")

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        elif self.den < 0:
            return str(-self.num) + "/" + str(-self.den)
        else:
            return str(self.num) + "/" + str(self.den)

    def print(self):
        if self.den == 1:
            print(self.num)
        elif self.den < 0:
            print(-self.num, "/", -self.den)
        else:
            print(self.num,"/",self.den)

    def simplify(self):
        common = gcd(self.num,self.den)
        newnum = self.num//common
        newden = self.den//common
        return Rational(newnum, newden)

    def __add__(self, other):
        return Rational(self.num*other.den + self.den*other.num, \
                        self.den*other.den)
        
    def __mul__(self, other):
        return Rational(self.num*other.num, self.den*other.den)
    
    def __neg__(self):
        return Rational(-self.num, self.den)
    
    def __sub__(self, other):
        return Rational(self.num*other.den - self.den*other.num, \
                        self.den*other.den)
    
    def reciprocal(self):
        return Rational(self.den,self.num)

    def __truediv__(self, other):
        return Rational(self.num*other.den, self.den*other.num)
    
    def __pow__(self,power):
        return Rational(self.num**power, self.den**power)
    
    def __eq__(self, other):
        return (self.num * other.den == other.num * self.den)
    
    def __ne__(self, other):
        return (self.num * other.den != other.num * self.den)
    
    def __lt__(self, other):
        temp1 = Rational(self.num, self.den)
        temp2 = Rational(other.num, other.den)
        if (temp1.den < 0):
            temp1.num = -temp1.num
            temp1.den = -temp1.den
        if(temp2.den < 0):
            temp2.num = -temp2.num
            temp2.den = -temp2.num
        return temp1.num*temp2.den < temp2.num*temp1.den
    
    def __le__(self, other):
        temp1 = Rational(self.num, self.den)
        temp2 = Rational(other.num, other.den)
        if (temp1.den < 0):
            temp1.num = -temp1.num
            temp1.den = -temp1.den
        if(temp2.den < 0):
            temp2.num = -temp2.num
            temp2.den = -temp2.num
        return temp1.num*temp2.den <= temp2.num*temp1.den
    
    def __gt__(self, other):
        temp1 = Rational(self.num, self.den)
        temp2 = Rational(other.num, other.den)
        if (temp1.den < 0):
            temp1.num = -temp1.num
            temp1.den = -temp1.den
        if(temp2.den < 0):
            temp2.num = -temp2.num
            temp2.den = -temp2.num
        return temp1.num*temp2.den > temp2.num*temp1.den
        
    def __ge__(self, other):
        temp1 = Rational(self.num, self.den)
        temp2 = Rational(other.num, other.den)
        if (temp1.den < 0):
            temp1.num = -temp1.num
            temp1.den = -temp1.den
        if(temp2.den < 0):
            temp2.num = -temp2.num
            temp2.den = -temp2.num
        return temp1.num*temp2.den >= temp2.num*temp1.den