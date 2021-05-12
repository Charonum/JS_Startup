import random
choices_list = []
while True:
    mylist = ["Saulo", "Maria", "Fernando"]
    choice = random.choice(mylist)
    if choice in choices_list:
        pass
    elif len(choices_list) == 3:
        choices_list = []
    else:
        mylist.append(choices_list)
        print(f"Give the item to {choice}")
