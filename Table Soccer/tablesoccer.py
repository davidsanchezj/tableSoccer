import turtle
import winsound

# Basic Setup

wn = turtle.Screen()
wn.title("Table Soccer by @davidsanchezj")
wn.setup(width=1152, height=648)
wn.bgpic("background.gif")
wn.tracer(0)

# Score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=1.8)
paddle_a.penup()
paddle_a.goto(-215,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=1.8)
paddle_b.penup()
paddle_b.goto(215,0)

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,290)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.shapesize(stretch_wid=1.5)
ball.penup()
ball.goto(0,0)

ball.dx = 0.3
ball.dy = 0.3

# Movement of the paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)   

# Keyboard binding

# Player A

wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_a_right, "d")

# Player B

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_left, "Left")
wn.onkeypress(paddle_b_right, "Right")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 270:
        ball.sety(270)
        ball.dy *= -1.001

    if ball.ycor() < -260:
        ball.sety(-260)
        ball.dy *= -1.001

    if ball.xcor() > 220:
        ball.setx(220)
        ball.dx *= -1.001
    
    if ball.xcor() < -220:
        ball.setx(-220)
        ball.dx *= -1.001
    
    # Goal
    if ball.xcor() > 210 and ball.xcor() < 230 and ball.ycor() > -40 and ball.ycor() < 40:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a +=1
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -210 and ball.xcor() > -230 and ball.ycor() > -40 and ball.ycor() < 40:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > paddle_b.xcor() + 0.2 or ball.xcor() < paddle_b.xcor() - 0.2) and (ball.ycor() < paddle_b.ycor() + 0.2 and ball.ycor() > paddle_b.ycor() - 0.2):
        ball.dx *= -1

    if (ball.xcor() > paddle_a.xcor() - 0.2 or ball.xcor() < paddle_a.xcor() + 0.2) and (ball.ycor() < paddle_a.ycor() + 0.2 and ball.ycor() > paddle_a.ycor() - 0.2):
        ball.dx *= -1
    