"""
Ordering machine
There is an empty menu order = []
1. Add new meals
example:
 ```
 Please enter the meal name: Burger
 Current order=['burger', 'burger']
 ```
2. Delete meals and remove all duplicate meals
example:
 After entering 2, it will be displayed
 ```
 Please enter the meal name: Burger
 Current order=[]
 ```
3. Submit the menu. When submitting, print out how many portions of each meal you ordered and end the program.
example:
 After entering 3, it will be displayed
 ```
 Burger:2
 French fries:1
 Coke:3
 ```
"""

order = []
while True:
    print("1. Add new meals")
    print("2. Delete meals and remove all duplicate meals")
    print(
        "3. Submit the menu. When submitting, print out how many portions of each meal you ordered and end the program."
    )
    choice = input("Please enter your choice: ")
    if choice == "1":
        order.append(input("Please enter the meal name: "))
        print("Current order = " + str(order))
    elif choice == "2":
        deletingorder = input("Please enter the meal name: ")
        c = order.count(deletingorder)
        for i in range(c):
            order.remove(deletingorder)
        print("Current order = " + str(order))
    elif choice == "3":
        print(order.count)
        break
    else:
        print("Please enter the correct choice")
