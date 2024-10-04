import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
screen.setup(700,490)
turtle.shape(img)
t = Turtle()
t.penup()
t.hideturtle()
game_is_on = True
states_guessed = []
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
while game_is_on:
    answer = screen.textinput(title=f"States guessed {len(states_guessed)}/50", prompt="Guess a State's name:").title()
    if answer == "Exit":
        for state in states_guessed:
            if state in all_states:
                all_states.remove(state)
        not_guessed_states = pandas.DataFrame(all_states)
        not_guessed_states.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        state_data = states[states.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        states_guessed.append(state_data.state.item())


