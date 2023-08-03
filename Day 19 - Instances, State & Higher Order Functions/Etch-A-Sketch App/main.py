from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclock():
    tim.circle(100,36)

def move_clockwise():
    tim.circle(-100,36)

def turn_right():
    tim.setheading(tim.heading() - 10)

def turn_left():
    tim.setheading(tim.heading() + 10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="z", fun=move_counterclock)
screen.onkey(key="x", fun=move_clockwise)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()