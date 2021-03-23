import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('red','yellow')
a=36
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.lt(a)
    t.bk(100)
    t.rt(a*3)
t.end_fill()

t.color('blue','gray')
t.penup()
t.bk(300)

t.pendown()
b=5
c=130 #1~180
a=(c*b-360)/b
t.begin_fill()
for i in range(b):
    t.fd(50)
    t.lt(a)
    t.bk(50)
    t.rt(c)
t.end_fill()
