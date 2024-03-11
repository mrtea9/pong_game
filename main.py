from turtle import Screen, Turtle
import time


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True

paddle = Turtle("square")
paddle.color("white")
paddle.turtlesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setpos(350, 0)

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
