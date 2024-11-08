for i in range(10, 1000):
    print(i)
else:
    print("loop will end normally")


# another version of the for loop:

u = 0
while u < 10:
    print(u)
    u += 1
else:
    print("loop will end normally")


"""
Create a countdown timer (in seconds) using a for loop.
- The user can enter a number of seconds.
- When the countdown reaches 0, display "Time's up!"

Example(in terminal):
---
Please enter the number of seconds: 3  
3  
2  
1  
Time's up! 

---

This way, the program will count down and show each second on the screen until it reaches zero.
"""
import time

seconds = int(input("Please enter the number of seconds: "))
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
else:
    print("Time's up!")

# another way to do the same thing:

import time

# while True:
#     seconds = int(input("Please enter the number of seconds: "))
#     if seconds == 0:
#         print("Time's up!")
#         break
#     for i in range(seconds, 0, -1):
#         print(i)
#         time.sleep(1)


# print(60 * 60 * 24  / 2)


# loop continue
for e in range(5):
    if i == 3:
        continue
    print(i)

else:
    i += 1


# Please enter the number of times you want to jump rope.
# The student is jumping rope, and when they reach multiples of 10 (like 10, 20, 30…), they take a break. Use `continue` to skip jumping when it is the 10th, 20th, 30th... time.

# Example:
# Please enter the number of times you want to jump rope: 15
# Jump 1 time
# Jump 2 times
# Jump 3 times
# Jump 4 times
# Jump 5 times
# Jump 6 times
# Jump 7 times
# Jump 8 times
# Jump 9 times
# Take a break
# Jump 11 times
# Jump 12 times
# Jump 13 times
# Jump 14 times
# Jump 15 times

import time

timesjump = int(input("Please enter the number of times you want to jump rope: "))
for i in range(timesjump):
    if i % 10 == 0:
        continue
    print(f"Jump {i} times")
    time.sleep(0.4)
else:
    print("Take a break")
    time.sleep(4.5)


# loop break
# ループをすぐ出るときはbreakを使う
# ただし、このブレークはそれが属するループのみに適用されることに注意してください
# したがって、まずこのブレークがどのループに属するかを判断する必要があります
# また　breakはループの最後であることを示すため、ループの最後にはbreakを使いません


for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(j)
    if i == 3:
        break
    print(i)

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
