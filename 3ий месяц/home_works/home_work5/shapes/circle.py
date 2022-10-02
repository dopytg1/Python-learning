import turtle
from shapes.shape import Shape

class Circle(Shape):
    def __init__(self, border, fill, coordinates, heading, radius):
        self.radius = radius
        super().__init__(border, fill, coordinates, heading)

    def draw(self):
        super().draw()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def __str__(self):
        super().__str__()
        print(f"Circle. Radius: {self.radius}")