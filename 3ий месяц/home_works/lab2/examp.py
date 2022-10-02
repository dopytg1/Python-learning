import math

class Fraction():
    def __init__(self, f_numerator, f_denominator):
        self.f_numerator = f_numerator
        self.f_denominator = f_denominator
        self.check_if_num()
        self.__normalize()
    
    def check_if_num(self):
        if not isinstance(self.f_numerator, int):
            raise TypeError("Числитель может быть только целым числом")
        if not isinstance(self.f_denominator, int):
            raise TypeError("Знаменатель может быть только целым числом")
        if self.f_denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

    def __normalize(self):
        k = math.gcd(self.f_numerator, self.f_denominator)
        self.f_numerator = self.f_numerator//k
        self.f_denominator = self.f_denominator//k

        if self.f_denominator < 0:
            self.f_numerator *= -1
            self.f_denominator *= -1

    def __add__(self, otherFraction):
        new_numerator = self.f_numerator * otherFraction.f_denominator + self.f_denominator * otherFraction.f_numerator
        new_denominator = self.f_denominator * otherFraction.f_denominator

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, otherFraction):
        new_num = self.f_numerator * otherFraction.f_denominator - self.f_denominator * otherFraction.f_numerator
        new_den = self.f_denominator * otherFraction.f_denominator

        return Fraction(new_num, new_den)

    def __mult__(self, otherFraction):
        new_num = self.f_numerator * otherFraction.f_numerator
        new_den = self.f_denominator * otherFraction.f_denominator

        return Fraction(new_num, new_den)

    def __truediv__(self, otherFraction):
        new_num = self.f_numerator * otherFraction.f_denominator
        new_den = self.f_denominator * otherFraction.f_numerator

        return Fraction(new_num, new_den)

    def __lt__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator < other_numerator

    def __le__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator <= other_numerator

    def __eq__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator == other_numerator    
        
    def __ne__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator != other_numerator

    def __gt__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator > other_numerator    
    
    def __ge__(self, otherFraction):
        f_numerator = self.f_numerator * otherFraction.f_denominator
        other_numerator = otherFraction.f_numerator * self.f_denominator

        return f_numerator >= other_numerator
        
    def __ceil__(self):
        if self.f_numerator % self.f_denominator > 0:
            return self.f_numerator // self.f_denominator + 1
        else:
            return self.f_numerator // self.f_denominator
    
    def __floor__(self):
        return self.f_numerator // self.f_denominator
    
    def __str__(self):
        numerator = self.f_numerator
        denominator = self.f_denominator

        string = f"{numerator}/{denominator}"
        if numerator < 0:
            new_str = "-"
            string = new_str + string
            numerator = -numerator

        if numerator > denominator:
            num = int(numerator / denominator)
            new_numerator = numerator - num * denominator
            if string[0] == "-":
                string = f"-{num} {new_numerator}/{denominator}"
            else:
                string = f"{num} {new_numerator}/{denominator}"

        print(string)


frac_1 = Fraction(25, 8)
frac_2 = Fraction(4, 2)

print(frac_1.__floor__())
f3 = frac_1 / frac_2

f3.__str__()