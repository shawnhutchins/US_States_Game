import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
correct_guess_count = 0
correct_guesses = []

game_is_on = True
while game_is_on:

    answer_state = (screen.textinput(
        title=f"{correct_guess_count}/50 States Correct",
        prompt="What's another state's name?")
        .title())
    print(answer_state)

    if answer_state in states.values:
        if answer_state in correct_guesses:
            print(f"You already correctly guessed {answer_state}")
        else:
            correct_guesses.append(answer_state)
            correct_guess_count += 1