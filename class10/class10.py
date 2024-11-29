import random as r

print(r.randrange(100))  # 0から９９の中からランダムな数を出力する
print(r.randrange(100, 200))  # 100から２００の中からランダムな数を出力する
print(r.randrange(0, 200))  # 0から２００の中からランダムな数を出力する
print(r.randrange(0, 100, 5))  # 0から９９の中から5ずつにランダムな数を出力する


"""

390 / 5,000
0 から 100 までの数字を入力してください: 50
大きすぎます
0 から 50 までの数字を入力してください: 25
大きすぎます
0 から 25 までの数字を入力してください: 15
小さすぎます
15 から 25 までの数字を入力してください: 30
大きすぎます
15 から 25 までの数字を入力してください: 10
小さすぎます
15 から 25 までの数字を入力してください: 20
小さすぎます
20 から 25 までの数字を入力してください: 23
小さすぎます
23 から 25 までの数字を入力してください: 24
できました! おめでとうございます!

"""

ans = r.randint(1, 100)
while True:
    x = int(input("数字を入力してください: "))
    if x == ans:
        print("できました! おめでとうございます!")
        break
    elif x < ans:
        print("小さすぎます")
    elif x > ans:
        print("大きすぎます")
    else:
        print("それはどうですか？")


# List
L = ["a", "b", "c", "d", "e"]
print(L[0])
print(L[1])
print(L[1:4:2])

for i in range(len(L)):
    print(L[i])

for e in L:
    print(e)


L[0] = "A"
print(L)

# listの中を変換する

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

# list+ listをする
L = [1, 2, 3]
L = L * 2
print(L)
