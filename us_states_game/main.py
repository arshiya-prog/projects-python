import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("/Users/arshiya/Desktop/Coding/Python/projects-python/us_states_game/blank_states_img.gif")

data = pandas.read_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/us_states_game/50_states.csv")
states_names = data["state"].to_list()
lower_names = [name.lower() for name in states_names]
no_of_correct_states = 0

game_is_on = True
already_visited = []

while game_is_on:
    name = screen.textinput(f"{no_of_correct_states}/50 states correct", "Enter state: ")
    if name:
        name = name.lower()

    if name == "exit":
        not_visited = [n for n in states_names if n.lower() not in already_visited]
        df_not_visited_states = pandas.DataFrame({"States Remaining": not_visited})
        df_not_visited_states.to_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/us_states_game/states_not_visted.csv")
        game_is_on = False

    if name in lower_names and name not in already_visited:
        already_visited.append(name)
        no_of_correct_states += 1
        state = data[data.state.str.lower() == name]

        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        tim.write(f"{state.state.iloc[0]}")

    if no_of_correct_states == 50:
        tim.goto(0,0)
        tim.write("YOU WIN!!!", align="center", font=("Calibri", 20, "bold"))
        game_is_on = False

screen.exitonclick()