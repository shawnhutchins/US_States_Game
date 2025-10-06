from turtle import Turtle

FONT = ("Arial", 10, "normal")

class NamePrinter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def print_name(self, name, cords):
        self.goto(cords)
        self.write(name, move=True, align="center", font=FONT)