from turtle import *

speed(40)
width(7)

color("brown")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()


#drowing a door
forward(70)
color("black")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#header
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
color("orange")
begin_fill()
left(30)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
penup()
goto(200, 200)
pendown()

forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()


exitonclick()

