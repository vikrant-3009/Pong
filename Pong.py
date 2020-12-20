import turtle

# SETTING UP THE SCREEN
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong by @Vikrant")
screen.setup(width=800, height=600)   
screen.tracer(0)                      # SPEED UP THE DRAWING OF COMPLEX GRAPHICS


# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4, stretch_len=0.8)
paddle_a.penup()                     # NO DRAWING OF LINE WHEN PADDLE IS MOVING
paddle_a.goto(-350, 0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4, stretch_len=0.8)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=0.8, stretch_len=0.8)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1 


# SCORE
score_a = 0
score_b = 0


# PEN (FOR DISPLAYING SCORE)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 22, "normal"))


# PADDLE A FUNCTIONS (FOR UP & DOWN MOVEMENT)
def paddle_a_up():
    y = paddle_a.ycor()        # RETURNS THE CURRENT Y COORDINATE OF THE TURTLE(i.e. PADDLE A)
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# PADDLE B FUNCTIONS (FOR UP & DOWN MOVEMENT)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# KEYBOARD BINDING
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")



# MAIN GAME LOOP
while True:
    screen.update()

    # MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # BORDER CHECKING (FOR PADDLE MOVEMENT)
    if paddle_a.ycor() >= 255:
        paddle_a.sety(255)

    if paddle_a.ycor() <= -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() >= 255:
        paddle_b.sety(255)

    if paddle_b.ycor() <= -250:
        paddle_b.sety(-250)

    # BORDER CHECKING (FOR BALL MOVEMENT)
    if(ball.ycor() >= 290):
        ball.dy *= -1
    
    if(ball.ycor() <= -285):
        ball.dy *= -1

    if(ball.xcor() >= 380):
        ball.goto(0, 0)
        ball.dx *= -1
        # SCORE UPDATE
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))

    if(ball.xcor() <= -390):
        ball.goto(0, 0)
        ball.dx *= -1
        # SCORE UPDATE 
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))

    # PADDLE AND BALL COLLISIONS
    if((ball.xcor() > 340) and (ball.xcor() < 348) and (ball.ycor() > paddle_b.ycor() - 51) and (ball.ycor() < paddle_b.ycor() + 51)):
        ball.dx *= -1
    
    if((ball.xcor() < -340) and (ball.xcor() > -348) and (ball.ycor() > paddle_a.ycor() - 51) and (ball.ycor() < paddle_a.ycor() + 51)):
        ball.dx *= -1
