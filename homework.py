"""
**Function Menu**
1. Add a subject and its score  
2. Delete a subject's score  
3. Exit the system  

In every step, show the current scores and the function menu.

---

**Example Terminal Output**:

```plaintext
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: English
Enter the score: 100
==========================
English: 100
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: Chinese
Enter the score: aaaaa
Invalid input, please enter a number.
Enter the score: 2
==========================
English: 100
Chinese: 2
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: Math
Enter the score: 55
==========================
English: 100
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 2
==========================
Enter the subject you want to delete: Science
This subject has not been added!
==========================
English: 100
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 2
==========================
Enter the subject you want to delete: English
Successfully deleted!
==========================
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 3
==========================
Chinese: 2
Math: 55
The average score is: 28.5
```
"""

score = {}
while True:
    print("1. Add a subject and score")
    print("2. Delete a subject's score")
    print("3. Submit all scores and show the average")
    choice = input("Please enter the function number: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid input, ple+ase enter a number.")
    if choice == "1":
        subject = int(input("Enter the subject you want to add: "))
        while True:
            try:
                score[subject] = int(input("Enter the score: "))
            except:
                print("Invalid input, please enter a string.")
                continue
            else:
                print(f"{subject}: {score[subject]}")
                break
    if choice == "2":
        deleting_subject = int(input("Enter the subject you want to delete: "))
        try:
            deleted_score = score.pop(deleting_subject)
        except:
            print("This subject has not been added!")
        else:
            print(f"Successfully deleted!")
            print(score)
