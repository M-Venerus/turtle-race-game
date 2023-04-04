import turtle as t
import random

race_running = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

new_y = -125
for new_color in colors:
    turt = t.Turtle(shape="turtle")
    turt.color_str = new_color
    turt.color(new_color)
    turt.penup()
    turt.goto(x=-200, y=new_y)
    turt.total_distance = 0
    all_turtles.append(turt)
    new_y += 50

if user_bet:
    race_running = True

while race_running:
    for tur in all_turtles:
        num = random.randint(1,10)
        tur.forward(num)
        tur.total_distance += num
        if tur.total_distance >= 450:
            winning_turt = tur.color_str
            race_running = False
            break
        
if user_bet == winning_turt:
    print(f"You got it right, the {winning_turt} turtle won!")
else: 
    print(f"Sorry, the {user_bet} turtle lost. The {winning_turt} turtle won.")






screen.exitonclick()