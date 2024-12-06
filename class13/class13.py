L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L.index(5))  # 4


L = [1, 9, 6, 5, 7, 8, 3, 4, 2, 10]
L.sort()  # 順番をそろえる
print(L)


print("---------------------------------------------------------")
L = [1, 9, 6, 5, 7, 8, 3, 4, 2, 10]
L.sort(reverse=True)  # 順番を逆にする
print(L)

dictionary = {
    "スマホ": 1,
    "カメラ": 2,
    "テレビ": 3,
    "ゲーム": 4,
    "太陽": 5,
    "水星": 6,
    "金星": 7,
    "地球": 8,
    "火星": 9,
}
print(dictionary["スマホ"])  # 1
print(len(dictionary))  # 9

print("---------------------------------------------------------")

print("地球" in dictionary)  # True
print("月" in dictionary)  # False

d = {"バナナ": 1, "オレンジ": 2, "レモン": 3}
for k in d:
    print(k)
    print(d[k])

for k in d.keys():
    print(k)
    print(d[k])

print("---------------------------------------------------------")


for v in d.values():
    print(v)

for k, v in d.items():
    print(f"{k}:{v}")

# class is doneクラスが終わりました
