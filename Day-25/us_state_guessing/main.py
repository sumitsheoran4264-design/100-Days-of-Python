import turtle
import pandas
#All states data
states_data = pandas.read_csv("Day-25/us_state_guessing/50_states.csv")
all_states = states_data["state"]
states_list = all_states.to_list()





# screen setup
screen = turtle.Screen()
image = "Day-25/us_state_guessing/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.color("black")

#Writer turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()




guessed_states = []

screen.title("U.S States Game")


continue_guessing = True

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Score: {len(guessed_states)}/50",
                                    prompt="What's the another state's name? ").title()
    
    if answer_state == "Exit":
        #After user type Exit save remaining state in csv 
        missing_state = [state for state in states_list if state not in guessed_states]
        df = pandas.DataFrame(missing_state, columns= ["state"])
        df.to_csv("Day-25/us_state_guessing/remaining_state.csv",index=False)
        break

    elif answer_state in states_list and not answer_state in guessed_states:
        state_row = states_data[states_data["state"] == answer_state]
        x_state = state_row["x"].iloc[0]
        y_state = state_row["y"].iloc[0]
        writer.goto(x_state, y_state)
        writer.write(answer_state)
        # if answer_state in state_list store answer in guessed_states
        guessed_states.append(answer_state)
        


screen.exitonclick()



