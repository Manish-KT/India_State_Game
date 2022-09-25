import turtle
import pandas

count = 0
screen = turtle.Screen()
screen.title("Indian States Games")
screen.addshape("india_map_raw.gif")
turtle.shape("india_map_raw.gif")
turtle2 = turtle.Turtle()
all_states = []
left_states = []
user_states = []


def game():
    user_input = screen.textinput(title="Guess India's States:>",
                                  prompt="Enter a state name or Exit to leave game").lower()

    data = pandas.read_csv("indian_states.csv")
    states = data.State
    all_states = states.values

    index = data.index[data["State"] == user_input].tolist()

    coor_x = data.loc[index, "X"]
    coor_y = data.loc[index, "Y"]
    x_cor_value = coor_x.values
    y_cor_value = coor_y.values

    for each in states.values:
        if user_input == each:
            user_states.append(user_input)
            turtle2.hideturtle()
            turtle2.penup()
            turtle2.goto(int(x_cor_value), int(y_cor_value))
            turtle2.color("red")
            turtle2.write(user_input.upper())

    if user_input == "exit":
        states_to_learn = {
            "States": list(set(all_states).difference(set(user_states)))
        }
        result = pandas.DataFrame(states_to_learn)
        result.to_csv("learn_these_states.csv")
        screen.exitonclick()
    else:
        game()


game()
