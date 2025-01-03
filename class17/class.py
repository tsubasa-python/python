a = ["a", "b", "c"]
b = a
# ｂはＡ　と同じの一つになる
b = [0]

print(a)


a = 10
b = a
b = 20
print(a)  # りすとでない場合は、リファクタリングされない


def add(a, b):
    return a + b


"""
このプログラムはAとBを引数にとり、A+Bを返す関数です。
"""


help(add)

"""
helpは、ドキュメントを表示します。
"""

print(add._doc_)


ans = eval("1 + 2")
print(ans)

ans = eval("数式を入力してください")
print(ans)
