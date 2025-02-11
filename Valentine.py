import turtle

turtle.colormode(255)

wn = turtle.Screen()
wn.bgcolor('#E39FF6')

shape = turtle.Turtle()
shape.hideturtle()
shape.color('red')




#Heart
shape.penup()
shape.setpos(0,-160)
shape.pendown()
shape.begin_fill()
shape.left(45)
shape.forward(250)
shape.circle(103, 225)
shape.left(180)
shape.circle(103, 225)
shape.forward(250)
shape.end_fill()
shape.penup()

shape.setpos(0,-50)
shape.pendown()
shape.color('white')
shape.write("CS",move=False,align='center',font=("Arial",120,("bold","normal")))

shape.penup()
shape.setpos(0,200)
shape.pendown()
shape.write("Will you be my",move=False,align='center',font=("Arial",80,("bold","normal")))

shape.penup()
shape.setpos(0,-250)
shape.pendown()
shape.write("Valentine?",move=False,align='center',font=("Arial",80,("bold","normal")))

wn.exitonclick()