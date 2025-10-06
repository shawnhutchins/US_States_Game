import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
correct_guesses = 0

game_is_on = True
while game_is_on:

    answer_state = (screen.textinput(
        title=f"{correct_guesses}/50 States Correct",
        prompt="What's another state's name?")
        .title())
    print(answer_state)

    if answer_state in states.values:
        correct_guesses += 1