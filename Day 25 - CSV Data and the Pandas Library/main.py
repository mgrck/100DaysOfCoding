import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = data.state.to_list()
xcor_list = data.x.to_list()
ycor_list = data.y.to_list()

score = 0
guessed_states = []

while score < 50:
    answer_state = (screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        i = states_list.index(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setpos(xcor_list[i], ycor_list[i])
        t.write(answer_state )
        score += 1