from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?, Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []


for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-210, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

            print(turtle.color)
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# tim = Turtle(shape="turtle")
# tim.color(colorss[0])
# tim.penup()
# tim.goto(x=-230, y= -150)
#
# tom = Turtle(shape="turtle")
# tom.color(colorss[1])
# tom.penup()
# tom.goto(x=-230, y= -90)
#
# tin= Turtle(shape="turtle")
# tin.color(colorss[2])
# tin.penup()
# tin.goto(x=-230, y= -30)
#
# tinny = Turtle(shape="turtle")
# tinny.color(colorss[3])
# tinny.penup()
# tinny.goto(x=-230, y= 30)
#
# tammy= Turtle(shape="turtle")
# tammy.color(colorss[4])
# tammy.penup()
# tammy.goto(x=-230, y= 90)
#
# torry= Turtle(shape="turtle")
# torry.color(colorss[5])
# torry.penup()
# torry.goto(x=-230, y= 150)
#
#
#






screen.exitonclick()
