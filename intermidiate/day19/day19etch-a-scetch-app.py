from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


def move_forwards():
    leo.forward(10)


def move_backwards():
    leo.backward(10)


def move_counter_clockwise():
    leo.left(10)


def move_clockwise():
    leo.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=leo.reset)

screen.exitonclick()