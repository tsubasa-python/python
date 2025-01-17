file = open("class18/file_test.py", "a")
file.write("\nprint('hello python')")
file.close()
# このように、ファイルを開くとCLOSEする必要がある

with open("class18/file_test.py", "a") as file:
    file.write("\nprint('hello python')")

# replaceは、文字列の一部を置換する。左＝右のように、マッチするものが置換される。
text = "hello python"
new_text = text.replace("python", "world")

text = "hello,world"
new_text = text.strip()
print(new_text)

# splitは、文字列を区切る。このように、カンマで区切られた文字列がリストに格納される。

text = "hello,world,python"
words = text.split(",")
print(words)
# このように、リストを取り出すと、文字列が変わる。
number = "7"
new_number = number.zfill(5)
print(new_number)


import datetime

now = datetime.datetime.now()
print(now)


date = datetime.datetime.strptime("2024/01/01", "%Y/%m/%d")
print(date)

# 有哪一些格式化字串可以使用？
# (What formatting strings can be used?)
# %Y - 年份（四位數）
# (Year (four digits))
# %m - 月份（兩位數）
# (Month (two digits))
# %d - 日期（兩位數）
# (Day (two digits))
# %H - 小時（24小時制，兩位數）
# (Hour (24-hour clock, two digits))
# %M - 分鐘（兩位數）
# (Minute (two digits))
# %S - 秒（兩位數）
# (Second (two digits))
# 例如：(For example:)
# %A - 星期幾的全名
# (Full name of the day of the week)
# %B - 月份的全名
# (Full name of the month)
# %c - 日期和時間的字串表示
# (String representation of date and time)
# %p - AM 或 PM
# (AM or PM)

date = datetime.datetime.now()
date_str = date.strftime("%Y-%m-%d")
print(date_str)


target_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d")
now = datetime.datetime.now()
days_left = (target_date - now).days
print(days_left)
