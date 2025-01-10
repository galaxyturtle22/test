import turtle as t

t.speed("fastest")
t.colormode(255)
t.speed(100)
t.hideturtle()
t.tracer(0, 0)

global c
c = 0


def get_color():
    global c 
    if i < 255:
        t.color(255, c, 0)

        c = c + 1
    elif i < 510:
        t.color(c,255,0)
        c = c - 1
    elif i < 765:
        t.color(0,255,c)
        c = c + 1
    elif i < 1020:
        t.color(0,c,255)
        c = c - 1
    elif i < 1275:
        t.color(c,0,255)
        c = c + 1
    elif i < 1530:
        t.color(255,0,c)
        c = c - 1
    

for i in range(0, 1530, 1):
    get_color()
    t.right(0.235294117647)
    t.forward(100)
    t.dot(10)
    t.forward(-100)
    
t.update
t.Screen().exitonclick()