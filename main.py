import turtle
import time
import random
import sys

def twopointfive():
    ranint = random.randint(0, 1)
    if ranint == 0:
        return -2.5
    else:
        return 2.5

screen = turtle.Screen()
screen.title("pong.")
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

ball = turtle.Turtle()
ball.speed(4)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.direction = "Stop"
ball.dx = twopointfive()
ball.dy = twopointfive()

p1score = 0
p2score = 0
score = turtle.Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 180)

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

point = 2
run = True
score.write(f"{p1score} | {p2score}", align="center", font=("Arial", 16))
while run:
    try:
        while p1score < point and p2score < point: #this should be an or lowk but tha makes it not work
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            if ball.ycor() > 220 or ball.ycor() < -220:
                ball.dy *= -1
            if ball.xcor() > 310 or ball.xcor() < -310:
                if ball.xcor() > 310:
                    p1score += 1
                else:
                    p2score += 1
                score.clear()
                score.write(f"{p1score} | {p2score}", align="center", font=("Arial", 16))
                ball.goto(0, 0)
                rpaddle.goto(200, 0)
                lpaddle.goto(-200, 0)
                screen.update()
                if p1score > point - 1 or p2score > point - 1:
                    break
                else:
                    time.sleep(1)
                    rpaddle.goto(200, 0)
                    lpaddle.goto(-200, 0)
                    ball.dx = twopointfive()
                    ball.dy = twopointfive()
            if rpaddle.ycor() > 220:
                rpaddle.sety(220) 
            elif rpaddle.ycor() < -220:
                rpaddle.sety(-220)
            if lpaddle.ycor() > 220:
                lpaddle.sety(220) 
            elif lpaddle.ycor() < -220:
                lpaddle.sety(-220)
            ball.dx *= 1.0005
            ball.dy *= 1.0005
            time.sleep(0.016)
            screen.update()
        screen.clear()        
        screen.bgcolor("#000000")
        score.goto(0, 0)
        if p1score > point - 1:
            score.write("Player 1 won!", align="center", font=("Arial", 30))
        elif p2score > point - 1:
            score.write("Player 2 won!", align="center", font=("Arial", 30))
        else:
            score.color("red")
            score.write("Something went pretty wrong here, please report", align="center", font=("Arial", 30))
           
        time.sleep(5)
        sys.exit()

    except turtle.Terminator:
        run = False