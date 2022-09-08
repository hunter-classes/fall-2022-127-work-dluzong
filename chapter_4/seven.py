import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()

pirate.penup()
pirate.forward(60)

pirate.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)

print("The pirate's final heading was", pirate.heading())

wn.exitonclick()
