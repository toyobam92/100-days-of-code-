import turtle
import pandas as pd
import time

states_game = pd.read_csv("50_states.csv")
FONT = ("Courier", 12, "normal")

states_dict = states_game.to_dict(orient='records')
all_states = states_game["state"]
list_states = all_states.to_list()

timmy = turtle.Turtle()
tammy = turtle.Turtle()
tim = turtle.Turtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def states_game():
    right_tries = 0
    wrong_tries = 0
    tammy.penup()
    screen.tracer(0)

    tammy.goto(100, 280)
    tammy.hideturtle()
    tammy.write(f"Right tries{right_tries}/50", align="center", font=("Courier", 20, "normal"))
    tim.goto(100, 260)
    tim.write(f"Wrong tries{wrong_tries}", align="center", font=("Courier", 20, "normal"))
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title="Guess the state", prompt="Whats another state name ?").title()

        if answer_state == "Exit":
            missing_states = []
            for state in list_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pd.dataframe(missing_states)
            new_data.to_csv("states_to_learn.csv")

        for dic in states_dict:
            for key in dic:
                if dic[key] == answer_state:

                    right_tries += 1
                    tammy.clear()
                    tammy.hideturtle()
                    tammy.write(f"Right tries{right_tries}/50", align="right", font=("Courier", 20, "normal"))

                    guessed_states.append(dic[key])
                    x = dic['x']
                    y = dic['y']
                    timmy.hideturtle()
                    timmy.penup()
                    timmy.goto(x, y)
                    timmy.write(answer_state, align='center', font=FONT)
                elif answer_state not in list_states and answer_state != "Exit":
                    wrong_tries += 1
                    tim.clear()
                    tim.write(f"Wrong tries{wrong_tries}", align="left", font=("Courier", 20, "normal"))


states_game()
screen.exitonclick()
