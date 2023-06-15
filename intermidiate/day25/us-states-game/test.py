import turtle
import pandas

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read in the data
data = pandas.read_csv("50_states.csv")

# List to keep track of guessed states
guessed_states = []

# Loop until all states are guessed
while len(guessed_states) < 50:
    # Get user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # Check if state is in data and not already guessed
    if answer_state in data.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_row = data[data["state"] == answer_state]
        state_x = int(state_row["x"])
        state_y = int(state_row["y"])

        # Write the state name on the screen
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

# Once all states are guessed, display a message and exit the screen
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, 0)
t.write("Congratulations! You guessed all 50 states!", align="center", font=("Arial", 16, "normal"))
screen.exitonclick()