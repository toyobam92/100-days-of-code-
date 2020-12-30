import colorgram
from turtle import Turtle, Screen, colormode
import random

#color = colorgram.extract('image.jpg', 100)

# color_list = []
# for i in range(len(color)):
#     #print(color[i].rgb)
#     color_list.append(color[i].rgb)
# print(color_list)

# rgb_colors = []
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
colormode(255)
color_list = [(208, 159, 108), (223, 206, 117), (136, 173, 194), (217, 232, 241), (38, 106, 140), (137, 184, 146), (13, 52, 76), (220, 87, 63), (146, 80, 71), (69, 165, 119), (29, 129, 106), (125, 80, 96), (9, 59, 50), (54, 153, 180), (197, 130, 144), (52, 33, 43), (129, 36, 49), (207, 83, 101), (4, 111, 88), (175, 206, 167), (156, 152, 69), (230, 167, 182), (144, 204, 233), (34, 64, 101), (46, 30, 26), (13, 87, 105), (183, 189, 204), (99, 41, 38), (223, 177, 167), (102, 129, 157), (67, 65, 57), (232, 198, 21)]
color_len = len(color_list)
timmy_the_turtle = Turtle()

colormode(255)
#
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)

screen = Screen()
screen.exitonclick()
