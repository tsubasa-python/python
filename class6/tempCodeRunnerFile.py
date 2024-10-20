import turtle as t

t.penup()
t.shape("square")
t.color("red")
for i in range(180):
    t.stamp()
    t.right(50)
    t.forward(7 + i)
t.done()