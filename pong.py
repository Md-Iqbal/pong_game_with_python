import turtle
import winsound

window = turtle.Screen()
window.title("Pong'2020")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# left bat

left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape("square")
right_bat.color("blue")
left_bat.shapesize(stretch_len=.7, stretch_wid=6)
left_bat.penup()
left_bat.goto(-390, 0)


# left bat function
# moving upwards
def left_bat_upwards():
    y = left_bat.ycor()
    y += 20
    left_bat.sety(y)


# moving downwards
def left_bat_downwards():
    y = left_bat.ycor()
    y -= 20
    left_bat.sety(y)


# right bat

right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape("square")
right_bat.color("blue")
right_bat.shapesize(stretch_len=.7, stretch_wid=6)
right_bat.penup()
right_bat.goto(380, 0)


# right bat function
# moving upwards


def right_bat_upwards():
    y = right_bat.ycor()
    y += 20
    right_bat.sety(y)


# moving downwards


def right_bat_downwards():
    y = right_bat.ycor()
    y -= 20
    right_bat.sety(y)


# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_len=.7, stretch_wid=.7)
ball.penup()
ball.goto(0, 0)
ball.dx = .2  # ball movement in x axis and d for derivative may be
ball.dy = -.2  # ball movement in y axis and d for derivative may be

# dividor

dividor = turtle.Turtle()
dividor.shape("square")
dividor.color("red")
dividor.shapesize(stretch_len=.09, stretch_wid=30)
dividor.goto(-0, -50)

# scorebord

# pen write
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player on LEFT: 0 |<>| Player on RIGHT: 0",
          align="center", font=("Arial", 20, "italic"))
left_score = 0
right_score = 0

# underline

underline = turtle.Turtle()
underline.shape("square")
underline.color("orange")
underline.shapesize(stretch_len=40, stretch_wid=.09)
underline.goto(0, 250)

# key board binding

window.listen()
window.onkeypress(left_bat_upwards, "w")
window.onkeypress(left_bat_downwards, "s")
window.onkeypress(right_bat_upwards, "Up")
window.onkeypress(right_bat_downwards, "Down")

# game loop
while True:
    window.update()

    # ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border bound
    if ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1
        winsound.PlaySound("pong_hit.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong_hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        left_score += 1
        pen.clear()
        pen.write("Player on LEFT: {} |<>| Player on RIGHT: {}".format(left_score, right_score),
                  align="center", font=("Arial", 20, "italic"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        right_score += 1
        pen.clear()
        pen.write("Player on LEFT: {} |<>| Player on RIGHT: {}".format(left_score, right_score),
                  align="center", font=("Arial", 20, "italic"))

    # bat & ball hitting logic

    if (ball.xcor() > 370 and ball.xcor() < 380) and (
            ball.ycor() < right_bat.ycor() + 40 and ball.ycor() > right_bat.ycor() - 40):
        ball.setx(370)
        ball.dx *= -1
        winsound.PlaySound("pong_hit.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -370 and ball.xcor() < -380) and (
            ball.ycor() < left_bat.ycor() + 40 and ball.ycor() > left_bat.ycor() - 40):
        ball.setx(-370)
        ball.dx *= -1
        winsound.PlaySound("pong_hit.wav", winsound.SND_ASYNC)
