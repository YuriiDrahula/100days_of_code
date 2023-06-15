# import colorgram
import turtle
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 40)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
from random import choice
from turtle import Turtle, Screen
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]
turtle.colormode(255)
point = Turtle()
point.speed("fastest")

point.penup()
point.setheading(225)
point.forward(300)
point.setheading(0)


number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    point.dot(20, choice(color_list))
    point.penup()
    point.forward(50)

    if dot_count % 10 == 0:
        point.hideturtle()
        point.setheading(90)
        point.forward(50)
        point.setheading(180)
        point.forward(500)
        point.setheading(360)


screen = Screen()
screen.exitonclick()