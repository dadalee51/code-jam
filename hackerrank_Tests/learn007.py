import turtle
t = turtle.Turtle()
t.shape('turtle')
t.fillcolor('yellow')
t.begin_fill()
#please play with the code, when in the for-loop all code should be indented by 1 tab. (the "->|" key)
for i in range(3):
    t.fd(100)
    t.lt(60)
    t.bk(100)
    t.lt(60)
    t.fd(100)
#getting out of for loop by dedent (going back 1 tab)
t.end_fill()

