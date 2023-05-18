import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300,700)

start_x = 0
start_y = 0
end_x = 0
end_y = 0

# white turtle
class Maze(turtle.Turtle):
    def __init__(self) -> None:
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)