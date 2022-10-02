import turtle
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.square import Squere
from shapes.triangle import Triangle


class Drawing():
    def __init__(self, shapes, bg):
        self.shapes = shapes
        self.bg = bg

    def draw(self):
        turtle.Screen().bgcolor(self.bg)
        turtle.hideturtle()
        turtle.speed(0)
        for each in self.shapes:
            each.__str__()
            each.draw()

        turtle.done()

shap = []

circ = Circle("white", 1, [0, 0], 0, 30)
cir1 = Circle("white", 1, [0, 55], 0, 15)
cir2 = Circle("white", 1, [0, -110], 0, 60)

line = Circle("white", 1, [10, 70], 0, 0)
yae1 = Circle("black", 1, [10, 70], 0, 3)
line2 = Circle("white", 1, [-10, 70], 0, 0)
yae2 = Circle("black", 1, [-10, 70], 0, 3)



button = Squere("black", 1, [0, 0], 0, 3)

button2 = Squere("black", 1, [0, 10], 0, 3)

line3 = Circle("white", 1, [0, 20], 0, 0)
button3 = Squere("black", 1, [0, 20], 0, 3)

shap.append(cir2)
shap.append(circ)
shap.append(cir1)

shap.append(line)
shap.append(yae1)
shap.append(line2)
shap.append(yae2)

shap.append(line3)
shap.append(button3)
shap.append(button2)
shap.append(button)

test = Drawing(shap, "black")
test.draw()