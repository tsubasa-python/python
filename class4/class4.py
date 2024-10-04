print(1 == 2)  # false #同じかどうかを判断する
print(1 != 2)  # true#同じでないかどうかを判断する
print(1 < 2)  # true#小さいかどうかを判断する
print(1 > 2)  # false#大きいかどうかを判断する
print(1 <= 2)  # true#1 is less than or equal to 2
print(1 >= 2)  # false#1 is greater than or equal to 2
print("---------------------------------------------------------")
print(True and True)  # true and true はすべての条件を満たすときにtrueを返す
print(True and False)  # true and false は一つの条件を満たしているときにfalseを返す
print(False and False)  # false and false はすべての条件を満たさないときにfalseを返す
print("---------------------------------------------------------")
print(True or True)  # true or true はいずれかの条件を満たすときにtrueを返す
print(True or False)  # true or false はいずれかの条件を満たしているときにtrueを返す
print(False or False)  # false or false はすべての条件を満たさないときにfalseを返す
print("---------------------------------------------------------")
print(not True)  # not true はfalseを返す
print(not False)  # not false はtrueを返す
print("---------------------------------------------------------")
password = input("パスワードを入力してください: ")
if password == "150126":
    print("パスワードが正しいです。")
else:
    print("パスワードが間違っています。")
print("---------------------------------------------------------")
pwd = input("パスワードを入力してください: ")
if pwd == "150126":
    print("こんにちは、alexさん。")
elif pwd == "123456":
    print("こんにちは、お兄さん。")
elif pwd == "1029384756":
    print("こんにちは、お姉さん。")
elif pwd == "1357924680":
    print("こんにちは、harukiさん。")
else:
    print("パスワードが間違っています。")
print("---------------------------------------------------------")
score = int(input("請輸入成績:"))
if score > 100:
    print("100以下の成績を入力してください。")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 0:
    print("０以上の成績を入力してください。")
else:
    print("F")
