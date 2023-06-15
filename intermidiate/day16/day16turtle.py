from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.shapesize(10, 10, 30)
timmy.turtlesize(7)
timmy.color("red", "green")

timmy.forward(250)
timmy.left(100)
timmy.forward(400)
timmy.left(100)
timmy.forward(700)
timmy.left(120)
timmy.forward(700)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()