import turtle

#def hexagon(fill in these):
#code to draw the hexagon
def hexagon(t, x, y, w, color, sidelen):
    """
  Draw a hexagon using the turtle passed into t
  Parameters:
    t - a turtle
    x,y - location
    w - width of side
    color - color to draw in
    sidelen - length of each side
  Returns:
    nothing
  
  """
    #set location, color, and width
    t.penup()
    t.goto(x, y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw a hexagon
    for i in range(6):
        t.forward(sidelen)
        t.right(60)


#def ngon(t,numsides,x,y,color,width,sidelen):
#code to draw the ngon
def ngon(t, numsides, x, y, w, color, sidelen):
    """
  Draw a ngon using the turtle passed into t
  Parameters:
    t - a turtle
    x,y - location
    w - width of side
    color - color to draw in
    sidelen - length of each side
  Returns:
    nothing
  
  """
    #set location, color, and width
    t.penup()
    t.goto(x, y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw a ngon
    
    for i in range(numsides):
        t.forward(sidelen)
        t.left(360 / numsides)


shape1 = turtle.Turtle()

hexagon(shape1, 70, -20, 2, "blue", 40)

shape2 = turtle.Turtle()
ngon(shape2, 8, -50, 50, 1, "red", 30)

wn = turtle.Screen()

wn.exitonclick()
wn.mainloop()
