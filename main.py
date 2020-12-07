from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
y = -150
all_turtles = []

for turtle_name in range(7):
  new_turtle = Turtle('turtle')
  new_turtle.color(colors[turtle_name])
  new_turtle.penup()
  new_turtle.goto(x=-230,y=y)
  y += 50
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:



  for turtle in all_turtles:

    if turtle.xcor()>230:
      is_race_on = False
      winning_turtle = turtle.pencolor()
      if winning_turtle == user_bet:
        print(f"You've won! The {winning_turtle} turtle won the race!")
      else:
        print(f"You've lost! The {winning_turtle} turtle won the race!")

    turtle.forward(random.randint(0, 10))

screen.exitonclick()