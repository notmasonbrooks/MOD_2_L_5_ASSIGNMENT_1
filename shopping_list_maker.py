def add_items(item):
    shopping_list.append(item)


def remove_items(item):
    shopping_list.remove(item)


def display_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")


shopping_list = []

while True:
    print("-Shopping List App-")
    print("Please choose an option:")
    print("[1] Add item to list")
    print("[2] Remove item from list")
    print("[3] Display shopping list")
    print("[4] Quit")
    choice = input("")
    if choice == "1":
        new_item = input("Please enter the item you would like to add:\n")
        add_items(new_item)
        print(f"{new_item} added to list.")
    elif choice == "2":
        new_item = input("Please enter the item you would like to remove:\n")
        if new_item not in shopping_list:
            print(f"Sorry, we can't find {new_item} in the shopping list.")
        else:
            remove_items(new_item)
            print(f"{new_item} removed from list.")
    elif choice == "3":
        display_list()
    elif choice == "4":
        break
    else:
        print("Invalid Input")
