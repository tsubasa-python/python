import turtle as t

t.speed(0)
t.penup()
t.shape("square")
t.color("red")
for i in range(4000):
    t.stamp()
    t.right(50)
    t.forward(7 + i)
t.done()