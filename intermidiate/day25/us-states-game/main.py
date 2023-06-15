import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"Guessed: {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()

    for i, row in data.iterrows():
        state = row["state"]
        if answer_state == state and state not in guessed_states:
            guessed_states.append(state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("black")
            t.goto(row["x"], row["y"])
            t.write(state, move=False, align="center", font=("Arial", 10, "normal"))

    if answer_state == "Exit":
        missing_states = []
        for i, row in data.iterrows():
            if row["state"] not in guessed_states:
                missing_states.append(row["state"])
                ms = turtle.Turtle()
                ms.hideturtle()
                ms.penup()
                ms.color("black")
                ms.goto(row["x"], row["y"])
                ms.write(row["state"], move=False, align="center", font=("Arial", 10, "normal"))
                ms.speed(0)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
