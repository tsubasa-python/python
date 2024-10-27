i = 0  # when i is lower than 10000, print i, and it will be repeated until i = 10000
while i < 10000:
    print(i)
    i = i + 1

print("--------------------------------------------------")


# +=, -=, *=, /=, %=, **=, //=
# x = x  + 1 can also be written as x += 1
# x = x - 1 can also be written as x -= 1
# x = x * 1 can also be written as x *= 1
# x = x / 1 can also be written as x /= 1
# x = x % 1 can also be written as x %= 1
# x = x ** 1 can also be written as x **= 1
# x = x // 1 can also be written as x //= 1

# uppgraded password door


user_input = ""
while user_input != "3.14":
    user_input = input("Enter your password: ")
print("Access granted")
