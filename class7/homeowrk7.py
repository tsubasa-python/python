"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""

num = int(input("請輸入正整數: "))
i = 1
while i <= num:
    if i % 3 == 0 or i % 7 == 0:
        print(i)
    i += 1


s = int(input("Please enter the size of the arrow: "))
for i in range(1, s + 1):
    print(" " * (s - i) + "*" * (2 * i - 1))
for n in range(s):
    print(" " * (s - 1) + "*")
