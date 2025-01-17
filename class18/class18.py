import os

# osは、ファイルやディレクトリの操作を行うモジュールです。さらにプログラムから出ることができる。
if os.path.exists("class18.py"):
    print("ありません")

else:
    print("あります")


# r - readは、ファイルを読み込むことができる。その前になければいけない。
# a - appendは、ファイルに文字列を追加することができる。
# w - writeは、最初っから書くことになる。
# r+は、読み込みと書き込みを行う。
# w+は, ないと最初っからファイルを書き込む。
# a+は、追加と書き込みを行う。


# class18/filetouse.pyを実行すると、このファイルの内容が表示される。
file = open("class18/file_test.py", "r")
print(file.read())
file.close()


with open("class18/file_test.py", "r") as file:
    print(file.read())
# このように、ファイルを開いて、ファイルの内容を表示すると、ファイルを閉じる必要がなくなる。

file = open("class18/file_test.py", "w")
file.write("print('something new!')")
file.close()
