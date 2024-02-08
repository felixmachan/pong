from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() != 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.sety(self.ycor() + 10)
