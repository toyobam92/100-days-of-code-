from turtle import Screen, Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITION:
            square = Turtle(shape="square")
            square.color('white')
            square.penup()
            square.goto(turtle_index)
            self.segments.append(square)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


        # for each_square in self.segments:
        #     screen = Screen()
        #     screen.listen()
        #     screen.onkey(key="Up", fun=each_square.forward())
        #     screen.onkey(key="Down", fun=each_square.backward())
        #     screen.onkey(key="Left", fun=each_square.left())
        #     screen.onkey(key="Right", fun=each_square.right())
        #

