import time

timesjump = int(input("Please enter the number of times you want to jump rope: "))
for i in range(timesjump):
    if i % 10 == 0:
        continue
    print(f"Jump {i} times")
    time.sleep(0.5)
else:
    print("Take a break")
