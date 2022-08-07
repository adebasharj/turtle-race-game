from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_axis = [-40, -70, -100, 40, 70, 100]
all_turtles = []
race_on = False
for turtles in range(0, 6):
    turtle_race = Turtle()
    turtle_race.penup()
    turtle_race.shape("turtle")
    turtle_race.goto(x=-230, y=y_axis[turtles])
    turtle_race.color(colors[turtles])
    all_turtles.append(turtle_race)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)











screen.exitonclick()