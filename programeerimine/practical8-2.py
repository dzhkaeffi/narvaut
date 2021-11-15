from turtle import *
title("The flag of Azerbaijan")
setup(800, 500)
speed(10)
up()
goto(-400, 250)
down()
# first color
color("dark blue")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()
right(180)
# second color
color("red")
up()
goto(-400, 83)
down()
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()
right(180)
# third color
color("SpringGreen4")
up()
goto(-400, -84)
down()
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

# moon
color("white")
up()
goto(-40, 80)
down()
begin_fill()
circle(80)
end_fill()
color("red")
up()
goto(-20, 66)
down()
begin_fill()
circle(65)
end_fill()

# star
color("white")
up()
goto(35, -8)
begin_fill()
for i in range(10):
    forward(25)
    right(150)
    forward(25)
    left(150)
    right(360 / 8)
end_fill()
hideturtle()
exitonclick()
