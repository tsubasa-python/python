s = int(input("Please enter the size of the arrow: "))

for i in range(1, s + 1):
    print(" " * (s - i) + "*" * (2 * i - 1))    
for n in range(s):
    print(" " * (s - 1) + "*")
