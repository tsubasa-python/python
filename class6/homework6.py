import time
import turtle as t

max = 0.5
t.shape("turtle")
t.speed(max)
t.penup()

for j in range(60):
    for i in range(1, 13):
        t.penup()
        t.forward(100)
        t.stamp()
        t.backward(100)
        t.left(30)

    print(6 * j)
    t.right(6 * j)
    t.pendown()
    t.forward(80)
    t.backward(80)
    time.sleep(1)
    t.clear()
    t.left(6 * j)
t.done()
