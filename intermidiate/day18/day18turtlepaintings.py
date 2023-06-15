import turtle
from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


# Challenge 1 - Draw a Square
for _ in range(4):
    timmy.forward(200)
    timmy.left(90)

# Challenge 2 - Draw a Dashed Line
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


# Challenge 3 - Draw different shapes
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(angles_amount):
    angles_degree = 360 / angles_amount
    for _ in range(angles_amount):
        timmy.forward(100)
        timmy.left(angles_degree)


for shape_side in range(3, 11):
    timmy.color(choice(colours))
    draw_shape(shape_side)


# Challenge 4 - Generate a random walk
timmy.width(10)
directions = [0, 90, 180, 270]


def random_walk():
    for _ in range(100):
        timmy.color(choice(colours))
        timmy.forward(25)
        timmy.setheading(choice(directions))


random_walk()
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colors = (r, g, b)
    return colors


# Challenge 5 - Draw a Spirograph
timmy.speed("fastest")
timmy.width(2)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(120)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)
        timmy.circle(120)


draw_spirograph(10)


screen = Screen()
screen.exitonclick()