import turtle
from shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, border, fill, coordinates, heading, first_lenght, second_length):
        super().__init__(border, fill, coordinates, heading)
        self.first_lenght = first_lenght
        self.second_length = second_length

    def draw(self):
        super().draw()
        turtle.begin_fill()
        turtle.forward(self.first_lenght)
        turtle.left(90)

        turtle.forward(self.second_length)
        turtle.left(90)

        turtle.forward(self.first_lenght)
        turtle.left(90)

        turtle.forward(self.second_length)
        turtle.end_fill()

    def __str__(self):
        super().__str__()
        print(f"Rectangle\n First lenght:{self.first_lenght}\n Second lenght: {self.second_length}")