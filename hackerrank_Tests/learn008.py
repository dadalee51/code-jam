import turtle
t = turtle.Turtle()
turtle.Screen().tracer(0)
t.shape('turtle')
t.fillcolor('yellow')
t.begin_fill()
#two level of indent (for loop)
for a in range(2):
    t.rt(5)
    for i in range(3):
        t.fd(100)
        t.lt(60)
        t.bk(100)
        t.lt(60)
        t.fd(100)
    print("done one shape")
print('all done, end filling~')
#getting out of for loop by dedent (going back 1 tab)
t.end_fill()

