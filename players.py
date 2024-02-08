from turtle import Turtle

STARTING_POSITION_1 = (-250,20)
STARTING_POSITION_2 =(250,20)

class Plate:

    def __init__(self):
        self.segments_1 = []
        self.segments_2 = []
        self.create_players()
        self.middle_line()

    def create_players(self):
            self.create_segment(1, STARTING_POSITION_1)
            self.create_segment(2, STARTING_POSITION_2)


    def create_segment(self,playernum, position):
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.setheading(90)
        new_segment.showturtle()
        if playernum == 1:
            self.segments_1.append(new_segment)
        if playernum == 2:
            self.segments_2.append(new_segment)

    def middle_line(self):
        line = Turtle()
        line.speed("fastest")
        line.hideturtle()
        line.penup()
        line.goto(0, -300)
        line.setheading(90)
        line.pendown()
        line.pencolor("white")
        while line.ycor() != 300:
            line.forward(5)
            line.penup()
            line.forward(5)
            line.pendown()


    def p1_move_up(self):
            self.segments_1[0].sety(self.segments_1[0].ycor() + 5)
            self.segments_1[1].sety(self.segments_1[1].ycor() + 5)
            self.segments_1[2].sety(self.segments_1[2].ycor() + 5)

    # def move(self):
    #         for seg_num in range(len(self.segments_1) - 1, 0, -1):
    #             new_x = self.segments_1[seg_num - 1].xcor()
    #             new_y = self.segments_1[seg_num - 1].ycor()
    #             self.segments_1[seg_num].goto(new_x, new_y)








