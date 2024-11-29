weather = ["Sunny", "Cloudy", "Rainy", "Sunny", "Cloudy", "Thunderstorm", "Sunny"]
while True:
    print(f"次の日の天気は{weather}です。")
    try:
        day = int(input("次の日の天気を選んでください: "))
    except:
        print("数字を入力してください")
        continue
    if day < 0 or day > 7:
        print("1-7の数字を入力してください")
        continue
    print(f"次の日の天気は{day}日目の天気です。")
    print(f"次の日の天気は{weather[day-1]}です。")
    new_weather = input("次の日の天気を選んでください: ")
    weather[day - 1] = new_weather
    print(f"正しい天気は{weather}")
    more = input("もっと天気を見てくださいか？(y/n): ")
    if more == "y":
        break
print("結果")
