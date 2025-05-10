# animation.py

import turtle

def draw_animation(screen):
    """Draws the anarchy symbol with a crown using Turtle."""
    t = turtle.RawTurtle(screen)
    t.speed(10)
    t.width(4)

    # Draw Circle
    t.pencolor("green")
    t.penup()
    t.goto(0, -130)
    t.pendown()
    t.circle(130)

    # Draw A
    t.speed(7)
    t.pencolor("green")
    t.width(5)
    t.penup()
    t.goto(-130, -120)
    t.pendown()
    t.goto(0, 180)  # Extended top
    t.goto(130, -120)
    t.penup()
    t.goto(-180, 45)  # Extended horizontal bar
    t.pendown()
    t.goto(180, 45)

    # Draw crown
    t.pencolor("gold")
    t.fillcolor("gold")
    t.penup()
    t.goto(-50, 190)  # Positioned higher above "A"
    t.pendown()
    t.begin_fill()
    t.goto(50, 190)
    for pos in [
        (-50, 190), (-40, 230), (-30, 200), (-20, 240), (-10, 210),
        (0, 250), (10, 210), (20, 240), (30, 200), (40, 230), (50, 190)
    ]:
        t.goto(pos)
    t.goto(-50, 190)
    t.end_fill()

    # Draw crown jewels
    t.width(2)
    t.pencolor("white")
    t.fillcolor("white")
    for x, y in [(-40, 240), (-20, 250), (20, 250), (40, 240)]:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.goto(x - 6, y - 8)
        t.goto(x, y - 16)
        t.goto(x + 6, y - 8)
        t.goto(x, y)
        t.end_fill()
    t.penup()
    t.goto(0, 260)
    t.pendown()
    t.begin_fill()
    t.goto(-12, 245)
    t.goto(0, 230)
    t.goto(12, 245)
    t.goto(0, 260)
    t.end_fill()
    t.hideturtle()

