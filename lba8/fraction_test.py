class Fraction:

    #initialize
    def __init__(self, init_numerator, init_denominator):
        self.numerator = init_numerator
        self.denominator = init_denominator

    #reciprocal
    def getReciprocal(self):
        reciprocal = Fraction(self.denominator, self.numerator)

        return reciprocal
    
    #multiply (XXX NOT as a FUNCTION... instead as a METHOD)
    def multiply(self, frac):
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator

        return Fraction(numerator, denominator)

    #compare fractions
    def compare(self, frac):
        if self.numerator / self.denominator > frac.numerator / frac.denominator:
            return 1
        elif self.numerator / self.denominator < frac.numerator / frac.denominator:
            return -1
        else:
            return 0
        
    #string method
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
        


frac1 = Fraction(1,2)
frac2 = Fraction(4,5)

print("frac1 * frac2:", frac1.multiply(frac2))

print("frac2 recip:", frac2.getReciprocal())

print("compare frac1 to frac2:", frac1.compare(frac2))