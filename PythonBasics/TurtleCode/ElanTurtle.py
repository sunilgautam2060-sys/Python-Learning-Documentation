import turtle
screenwindow=turtle.Screen()
screenwindow.bgcolor("lightgreen")

elan=turtle.Turtle()
elan.pensize(5)
elan.color("blue")
elan.shape("turtle")
distance=100
angle=90
for i in range(10):
 elan.forward(distance)
 elan.right(angle)
 distance=distance+10
 angle=angle-2

screenwindow.exitonclick()

