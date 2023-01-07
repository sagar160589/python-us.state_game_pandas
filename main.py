import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What's another state name").title()
    updated_user_answer = user_answer.capitalize()
    if updated_user_answer in all_states:
        coordinates = states_data[states_data.state == updated_user_answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(updated_user_answer)
        guessed_state.append(updated_user_answer)
    elif user_answer == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        missing = pandas.DataFrame(missing_states)
        missing.to_csv("missing_states.csv")
        break






screen.exitonclick()