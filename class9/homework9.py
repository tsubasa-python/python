"""
你製作了一台飲料機！這台飲料機有四個按鈕，每個按鈕都會給出不同的飲料：
蘋果汁 🍎
柳橙汁 🍊
葡萄汁 🍇
系統關閉 🔴
客人會按這些按鈕來選擇他們想要的飲料。
選擇後系統會告訴他們他們選了什麼飲料，但是，如果客人選擇了「系統關閉」，飲料機就會停止工作。
如果客人按錯了按鈕（也就是輸入了不正確的編號），你需要告訴他們「輸入錯誤查無此果汁，請重新輸入」。

範例（在終端機中）：
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:2
您點的商品是柳橙汁
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:3
您點的商品是葡萄汁
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:f
輸入錯誤查無此果汁，請重新輸入
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:4
~~系統關閉~~

"""

while True:
    print("メニュー")
    print("1. リンゴジュース")
    print("2. オレンジジュース")
    print("3. ぶどうジュース")
    print("4. システムのシャットダウン")

    choice = input("番号を入力してください: ")

    # 入力値が数字かどうかチェック
    if choice.isdigit():
        choice = int(choice)

        if choice == 4:
            print("システムを終了します")
            break
        elif 1 <= choice <= 3:
            print(f"あなたは{choice}番のドリンクを注文しました")
        else:
            print("無効な入力です。1から4の数字を入力してください")
    else:
        print("数字を入力してください")