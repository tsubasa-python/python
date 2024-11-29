print(range(10))  # rangeここでも使う
print(list(range(10)))  # 数字をリストにする
print(list("HELLO"))  # 一文字一文字のリストを作る


s = "Hello world"
L = s.split(" ")
print(L)
calandar = "2024/12/25"
L = calandar.split("/")
print(L)


L = ["hello", "world"]
s = " ".join(L)
print(s)


L = ["hello", "world"]  # リストの定義
L.append("world")  # リストに要素を追加
print(L)  # リストの要素を表示
L.remove("world")  # リストから要素を削除
print(L)  # リストの要素を表示

s = L.pop(0)
print(s)

L = ["hello", "world", "Python", "Hello"]
print(L.count("hello"))  # helloが出現する回数を表示
