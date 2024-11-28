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
    3.
    2. 柳橙汁
    3. 葡萄汁
    4. 系統關閉 葡萄汁
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
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")

    ans = input("請輸入編號:")
    if ans == "1":
        print("您點的商品是蘋果汁")
    elif ans == "2":
        print("您點的商品是柳橙汁")
    elif ans == "3":
        print("您點的商品是葡萄汁")
    elif ans == "4":
        print("~~系統關閉~~")
        break
    else:
        print("輸入錯誤查無此果汁，請重新輸入")
