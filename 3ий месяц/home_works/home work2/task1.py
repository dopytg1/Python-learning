class Rectangle:
    def __init__(self, rectSide1, rectSide2) -> None:
        self.rectSide1 = rectSide1
        self.rectSide2 = rectSide2

    def perimeter_count(self):
        return (self.rectSide1 + self.rectSide2) * 2
        

    def squere_count(self):
        return self.rectSide1 * self.rectSide2
         

    def description_rect(self):
        print("Первая сторона: %s\nВторая сторона: %s" %(self.rectSide1, self.rectSide2))
        print("Периметр: %s\nПлощадь: %s" %(self.perimeter_count(), self.squere_count()))


rect1 = Rectangle(10, 5)
print(rect1.perimeter_count())