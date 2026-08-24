import turtle

screenwindow=turtle.Screen()
screenwindow.bgcolor("lightgreen")
sunil=turtle.Turtle()
sunil.color("blue")
sunil.shape("turtle")

distance=5
sunil.up()

for _ in range(30):
    sunil.stamp()
    sunil.forward(distance)
    sunil.right(24)
    distance=distance+2
screenwindow.exitonclick()