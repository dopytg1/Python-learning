import turtle
from shapes.shape import Shape

class Triangle(Shape):
    def __init__(self, border, fill, coordinates, heading, length):
        self.length = length
        super().__init__(border, fill, coordinates, heading)

    def draw(self):
        super().draw()
        turtle.begin_fill()
        turtle.forward(self.length)

        turtle.left(120)
        turtle.forward(self.length)

        turtle.left(120)
        turtle.forward(self.length)
        turtle.end_fill()

    
    def __str__(self):
        super().__str__()
        print(f"Triangle. Lenght: {self.length}")