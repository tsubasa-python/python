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


thing = "Alex"  # globalを使ったので猫になる


def something():  # これは関数を定義している
    thing = "blablabla"
    print(thing)


def otherthing():
    global thing  # globalは変数を同期する
    thing = "猫"
    print(thing)


def somethingelse():
    global alex
    alex = "うｐ主"
    print(alex)


# globalは変数を同期する
