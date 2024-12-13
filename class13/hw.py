"""
Xiao-Hua's birthday is coming soon! He wants to have a special birthday party with his friends.
He has already decided what food to prepare and put the information in a dictionary, like this:
food_list = {"cake": 1, "sandwich": 10, "juice": 20, "french fries": 15, "pizza": 2}
The terminals will show the following information:
cake: 1 piece
sandwich: 10 pieces
juice: 20 cups
french fries: 15 portions
pizza: 2 pieces
"""

food_list = {"cake": 1, "sandwich": 10, "juice": 20, "french fries": 15, "pizza": 2}

for k, v in food_list.items():
    if k == "juice":
        print(f"{k}: {v} cups")
    else:
        print(f"{k}: {v} pieces")
