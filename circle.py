import turtle

space=turtle.Screen()


space.addshape("spaceman.gif")
spaceman=turtle.Turtle()
spaceman.shape("spaceman.gif")

spaceman.penup()
spaceman.goto(-103,255)


space.bgpic("back ground.gif")
space.addshape("rocket1.gif")
rocket=turtle.Turtle()
rocket.shape("rocket1.gif")


rocket.up()
rocket.goto(180,-250)
rocket.down()
rocket.speed(1000)
def up():
    rocket.setheading(90)
    rocket.forward(3)
    rocket.setheading(0)
    rocket.penup()

def down():
    rocket.setheading(270)
    rocket.forward(3)
    rocket.setheading(0)
    rocket.penup()

def right():
    rocket.setheading(0)
    rocket.forward(3)
    rocket.setheading(0)
    rocket.penup()

def left():
    rocket.setheading(180)
    rocket.forward(3)
    rocket.setheading(0)
    rocket.penup()

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()

while True:
    space.update()
    if rocket.distance(spaceman) <10:
        space.bgpic("win.gif")

        

turtle.done()