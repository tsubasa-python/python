import turtle as t

t.speed(0)
t.penup()
t.shape("turtle")
t.color("red")
for i in range(300):
    t.stamp()
    t.right(50)
    t.forward(7 + i)
t.done()

a = int(input("数字を入力してください。"))
sum = 0
for i in range(a + 1):
    sum = sum + i

print(f"0から{a}までの和は{sum}です。")
# repeat 4000 t.stamp() t.right(4800) t.forward(7 + i)
