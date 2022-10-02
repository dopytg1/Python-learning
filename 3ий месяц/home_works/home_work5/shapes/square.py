import turtle
from shapes.shape import Shape

class Squere(Shape):
    def __init__(self, border, fill, coordinates, heading, lenght):
        self.lenght = lenght
        super().__init__(border, fill, coordinates, heading)

    def draw(self):
        super().draw()
        turtle.begin_fill()
        turtle.forward(self.lenght)
        turtle.left(90)

        turtle.forward(self.lenght)
        turtle.left(90)

        turtle.forward(self.lenght)
        turtle.left(90)

        turtle.forward(self.lenght)
        turtle.end_fill()

    def __str__(self):
        super().__str__()
        print(f"Squere. lenght: {self.lenght}")