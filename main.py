import turtle
import pandas
from name_printer import NamePrinter

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name_printer = NamePrinter()

data = pandas.read_csv("50_states.csv")
states = data.state
correct_guesses = []

game_is_on = True
while game_is_on:

    answer_state = (screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct",
        prompt="What's another state's name?")
        .title())
    print(answer_state)

    if answer_state in states.values:
        if answer_state in correct_guesses:
            print(f"You already correctly guessed {answer_state}")
        else:
            state_row = data[data.state == answer_state]
            state_cords = (state_row.x.item(), state_row.y.item())
            state_name_printer.print_name(answer_state, state_cords)
            correct_guesses.append(answer_state)