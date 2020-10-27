import turtle
import random
#random.seed(10)
dia = 100
mid =  dia * pow(2,0.5) / 2
xdata = [   0,  mid, dia, mid]
ydata = [-dia, -mid,   0, mid]
turtle.pensize(5)
turtle.pencolor(random.random(),random.random(),random.random())
turtle.penup()
turtle.goto(0,-dia / 2)
turtle.pendown()
turtle.circle(dia,360)
for i in range(9):
    turtle.pencolor(random.random(),random.random(),random.random())
    turtle.penup()
    if i < 4 or i == 8:
        turtle.goto(xdata[i % 4],ydata[i % 4])
    else:
        turtle.goto(-xdata[i % 4],-ydata[i % 4])
    turtle.pendown()
    turtle.circle(dia / 2,360)
turtle.done()