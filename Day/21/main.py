from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
scores = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    #Detect collision
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scores.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scores.game_over()

    #Detect collisiion with tail
    #if head collides with any segemnt in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scores.game_over()


    # for seg in segments:
    #     seg.forward(20)
    #     #time.sleep(1)

# timmy = Turtle()
# timmy.shape("square")
# timmy.color("white")
#
# tommy = Turtle()
# tommy.shape("square")
# tommy.color("white")
# tommy.goto(x=-20, y=0)
#
#
# to = Turtle()
# to.shape("square")
# to.color("white")
# to.goto(x=20, y=0)










screen.exitonclick()