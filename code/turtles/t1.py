import turtle

wn = turtle.Screen()  #screen makes a window

crush = turtle.Turtle()  #makes a turtle

#draw a square
crush.color("blue")
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

#create a second turtle
#into the variable squirt
#and make squirt draw a triangle
squirt = turtle.Turtle()

squirt.up()
squirt.goto(50, 50)
squirt.down()
squirt.pensize(2)
squirt.color("red")
squirt.forward(50)
squirt.left(120)
squirt.forward(50)
squirt.left(120)
squirt.forward(50)
squirt.left(120)

wn.exitonclick()
wn.mainloop()

a = 10 + 30

#don't name your program turtle.py, it will be recognized as a module (like import turtle)

#you can upload files into github directly

#you can search up python turtle references for assistance
