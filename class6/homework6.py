import time
import turtle as t

t.shape("turtle")
t.speed(0)
t.penup()
for r in range(60):
    t.right(6)
    t.pendown()
    t.forward(80)
    t.penup()
    time.sleep(1)
    t.backward(80)
    t.clear()
    for i in range(12):
        t.forward(100)
        t.stamp()
        t.backward(100)
        t.left(30)


t.done()
