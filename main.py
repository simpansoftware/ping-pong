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
screen.title("ping pong")
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

start = turtle.Turtle()
start.shape("square")
start.shapesize(stretch_wid=4, stretch_len=8)
start.fillcolor("green")
start.penup()
start.hideturtle()
start.goto(-150, -30)

starttext = turtle.Turtle()
starttext.color("white")
starttext.hideturtle()
starttext.penup()
starttext.hideturtle()
starttext.goto(-190, -50)

quitter = turtle.Turtle()
quitter.shape("square")
quitter.shapesize(stretch_wid=4, stretch_len=8)
quitter.fillcolor("red")
quitter.penup() 
quitter.hideturtle()
quitter.goto(150, -30)

quittext = turtle.Turtle()
quittext.color("white")
quittext.hideturtle()
quittext.penup()
quittext.hideturtle()
quittext.goto(110, -50)

haha = turtle.Turtle()
haha.color("gray")
haha.penup()
haha.hideturtle()
haha.goto(0, 75)

heart = turtle.Turtle()
heart.color("gray")
heart.penup()
heart.hideturtle()
heart.goto(0, -220)

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
ballhalf = 10
score = turtle.Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 180)

titletext = turtle.Turtle()
titletext.color("white")
titletext.hideturtle()
titletext.penup()
titletext.goto(0, 100)

def down1():
    lpaddle.sety(lpaddle.ycor() - 20)

def up1():
    lpaddle.sety(lpaddle.ycor() + 20)

def down2():
    rpaddle.sety(rpaddle.ycor() - 20)

def up2():
    rpaddle.sety(rpaddle.ycor() + 20)

def clickstuff(x, y):
    global screen, startloop
    if -230 <= x <= -70 and -70 <= y <= 10:
        startbutton(x, y)
        screen.onclick(None)
    if 70 <= x <= 230 and -70 <= y <= 10:
        startloop = False
        sys.exit()

def startbutton(x, y):
    global startloop, run
    start.clearstamps()
    quitter.clearstamps()
    titletext.clear()
    heart.clear()
    haha.clear()
    starttext.clear()
    quittext.clear()
    ball.showturtle()
    rpaddle.showturtle()
    lpaddle.showturtle()
    score.write(f"{p1score} | {p2score}", align="center", font=("Arial", 16))
    startloop = False
    screen.update()
    time.sleep(1)
    run = True

def bounce(paddle):
    ball.dx *= -1
    if paddle == lpaddle:
        ball.setx(paddle.xcor() + 10 + 10)
    else:
        ball.setx(paddle.xcor() - 10 - 10)

    offset = (ball.ycor() - paddle.ycor()) / 50
    ball.dy += offset * random.uniform(1, 1.5)
    max_dy = abs(ball.dx) * 1.5
    if ball.dy > max_dy:
        ball.dy = max_dy
    elif ball.dy < -max_dy:
        ball.dy = -max_dy

screen.listen()
screen.onkeypress(up1, "w")
screen.onkeypress(down1, "s")
screen.onkeypress(up2, "Up")
screen.onkeypress(down2, "Down")
screen.onclick(clickstuff)

point = 10
run = False
startloop = True
start.stamp()
quitter.stamp()
titletext.write("ping pong", align="center", font=("Arial", 60))
starttext.write("Start", font=("Arial", 30))
quittext.write("Quit", font=("Arial", 30))
heart.write("Made with love by simpansoftware", align="center", font=("Arial", 10))
haha.write("(but mostly pong)", align="center", font=("Arial", 12))
ball.hideturtle()
rpaddle.hideturtle()
lpaddle.hideturtle()
screen.update()
while startloop:
    try:
        time.sleep(0.016)
        screen.update()
    except Exception:
        startloop=False
        sys.exit()
while run:
    try:
        while p1score < point and p2score < point: #this should be an or lowk but tha makes it not work
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            if ball.ycor() > 220 or ball.ycor() < -220:
                ball.dy *= -1
            if (ball.dx > 0 and ball.xcor() + 10 >= rpaddle.xcor() - 10) and ball.xcor() < rpaddle.xcor() and rpaddle.ycor() - 50 <= ball.ycor() <= rpaddle.ycor() + 50:
                bounce(rpaddle)
            if (ball.dx < 0 and ball.xcor() - 10 <= lpaddle.xcor() + 10) and ball.xcor() > lpaddle.xcor() and lpaddle.ycor() - 50 <= ball.ycor() <= lpaddle.ycor() + 50:
                bounce(lpaddle)
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
            ball.dx *= 1.001
            ball.dy *= 1.001
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

    except Exception:
        run = False
        sys.exit()