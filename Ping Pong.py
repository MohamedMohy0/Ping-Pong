import turtle

window=turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

stick1=turtle.Turtle()
stick1.speed(0)
stick1.shape("square")
stick1.color("orange")
stick1.penup()
stick1.goto(-380,0)
stick1.shapesize(stretch_wid=5,stretch_len=1)
stick2=turtle.Turtle()
stick2.speed(0)
stick2.shape("square")
stick2.color("blue")
stick2.penup()
stick2.goto(380,0)
stick2.shapesize(stretch_wid=5,stretch_len=1)
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3
score=turtle.Turtle()
score1=0
score2=0
score.speed(0)
score.color("green")
score.penup()
score.hideturtle()
score.goto(0,270)
score.write("player 1: 0 player 2: 0",align="center",font=("courier",24,"normal"))

def stick1_up():
    y=stick1.ycor()
    y+=20
    stick1.sety(y)
def stick1_down():
    y=stick1.ycor()
    y-=20
    stick1.sety(y)

def stick2_up():
    y=stick2.ycor()
    y+=20
    stick2.sety(y)
def stick2_down():
    y=stick2.ycor()
    y-=20
    stick2.sety(y)

window.listen()
window.onkeypress(stick1_up,"w")
window.onkeypress(stick1_down,"s")
window.onkeypress(stick2_up,"Up")
window.onkeypress(stick2_down,"Down")


while True:
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.dx*=-1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))
        score2+=1
    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.dx*=-1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))
        score1+=1
    if (ball.xcor()>370 and ball.xcor()<380) and (ball.ycor()<stick2.ycor()+40 and ball.ycor()>stick2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        
    if (ball.xcor()<-370 and ball.xcor()>-380) and (ball.ycor()<stick1.ycor()+40 and ball.ycor()>stick1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1