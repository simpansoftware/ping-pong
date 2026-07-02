import turtle
import time

screen = turtle.Screen()
screen.title("Ping")
screen.bgcolor("#000000")
screen.setup(width=640, height=480)
screen.tracer(0)
root = screen.getcanvas().winfo_toplevel()
root.resizable(False, False)

lpaddle = turtle.Turtle()
lpaddle.shape("square")
lpaddle.shapesize(stretch_wid=5, stretch_len=1)
lpaddle.color("white")
lpaddle.penup()
lpaddle.goto(-200, 0)
lpaddle.direction = "Stop"

rpaddle = turtle.Turtle()
rpaddle.shape("square")
rpaddle.shapesize(stretch_wid=5, stretch_len=1)
rpaddle.color("white")
rpaddle.penup()
rpaddle.goto(200, 0)
rpaddle.direction = "Stop"

rpaddle = turtle.Turtle()
rpaddle.shape("square")
rpaddle.color("white")
rpaddle.penup()
rpaddle.goto(0, 0)
rpaddle.direction = "Stop"

def down1():
    lpaddle.sety(lpaddle.ycor() - 20)

def up1():
    lpaddle.sety(lpaddle.ycor() + 20)

def down2():
    rpaddle.sety(rpaddle.ycor() - 20)

def up2():
    rpaddle.sety(rpaddle.ycor() + 20)

screen.listen()
screen.onkeypress(up1, "w")
screen.onkeypress(down1, "s")
screen.onkeypress(up2, "Up")
screen.onkeypress(down2, "Down")

run = True
while run:
    try:
        screen.update()

    except turtle.Terminator:
        run = False