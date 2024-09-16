from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.bgcolor('black')
screen.setup(width=600, height=600)

turtle.color('white')
turtle.penup()
turtle.setheading(90)

player_speed = 0


def move_left():
    global player_speed
    player_speed = -3


def move_right():
    global player_speed
    player_speed = 3


def stop():
    global player_speed
    player_speed = 0


screen.listen()
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")

screen.onkeyrelease(stop, "Right")
screen.onkeyrelease(stop, "Left")

while True:
    turtle.setx(turtle.xcor() + player_speed)



screen.exitonclick()