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
