import turtle
screenwindow=turtle.Screen()

#Turtle Object(Sunil) Description:
sunil=turtle.Turtle()
sunil.pensize(5)
sunil.color("blue")

#Sunil draws a rectangle
sunil.right(90)
sunil.forward(100)
sunil.right(90)
sunil.forward(80)
sunil.right(90)
sunil.forward(100)
sunil.right(90)
sunil.forward(80)
sunil.right(180) 

#Another Turtle Object(Pradip) Description:
pradip=turtle.Turtle()
pradip.pensize(3)
pradip.color("orange")

#Pradip draws a triangle at top
pradip.left(120)
pradip.forward(80)
pradip.left(120)
pradip.forward(80)
pradip.left(120)

#Holding the screen until user clicks on it to exit
screenwindow.exitonclick()  