import turtle

class Shape():
    def __init__(self, border, fill, coordinates, heading):
        self.border = border
        self.fill = fill
        self.coordinates = coordinates
        self.heading = heading

    def draw(self):
            turtle.color(self.border)
            turtle.pensize(self.fill)
            turtle.goto(self.coordinates)
            turtle.setheading(self.heading)

    def __str__(self):
        print(f"Coordinates: {self.coordinates}, Heading: {self.heading}, Border: {self.border}, Fill: {self.fill}")


shape = Shape('green', 2, [0, 0], 90)
shape.draw()