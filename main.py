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
states = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = (screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct",
        prompt="What's another state's name?")
        .title())

    if answer_state == "Exit":
        states_set = set(states)
        correct_guesses_set = set(correct_guesses)
        missed_states = list(states_set - correct_guesses_set)
        pandas.DataFrame(missed_states).to_csv("missed_states.csv")
        break
    if answer_state in states:
        if answer_state in correct_guesses:
            print(f"You already correctly guessed {answer_state}")
        else:
            state_row = data[data.state == answer_state]
            state_cords = (state_row.x.item(), state_row.y.item())
            state_name_printer.print_name(answer_state, state_cords)
            correct_guesses.append(answer_state)
