name = "Alex"  # 変数の定義


def say_hello():  # これは関数を定義している
    print("Hello, world!")
    print("Hello, world!")


say_hello()  # 関数を実行する


def say_hello(name):  # nameには引数を渡す
    print(f"Hello, {name}!")  # nameもプリントする
    print("nice to meet you")


say_hello("Alex")  # alex をnameに渡す


def say_hellowithdefault(name="Alex"):  # nameには引数を渡す
    print(f"Hello, {name}!")  # nameもプリントする
    print("nice to meet you")


print(f"Hello, {name}!")  # nameもプリントする

say_hellowithdefault("Alex")
print("\nこんにちわんこそば。")
# ちなみに\nは改行を表す
print(f"君の名は……{name}ですよね。")
# 君の名は……Alexですよね。とプリントする


def calculate(a, b=0):
    total = a + b
    return total


result = calculate(10, 20)
print(f"答えは{result}です。")
# 答えは30です。
result = calculate(10)
print(f"答えは{result}です。")


def 注文(メインディッシュ, サイドディッシュ="なんかおいしい肉"):
    print(f"メインディッシュは{メインディッシュ}です。")
    print(f"サイドディッシュは{サイドディッシュ}です。")


注文("牛肉", "サラダ")  # メインディッシュは牛肉です。サイドディッシュはサラダです。
