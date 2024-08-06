
''' 
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.
'''

def add_to_list():
    item = input("Item to add: ").lower()
    shopping_list.append(item)
    print(f"\n{item} added to list\n")

def remove_from_list():
    item = input("Item to remove: ").lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n{item} removed from list\n")
    else:
        print(f"\n{item} not found in list\n")

def print_entire_list():
    print("ITEMS:")
    if len(shopping_list) == 0:
        print("No items in list\n") 
    else:
        for item in shopping_list:
            print(f"- {item}")

shopping_list = []
while True:
    action = input("\nWhat would you like to do?\n[A]dd item to list\n[R]emove item from list\n[D]isplay list\n[Q]uit\n\n").lower()
    if action == "a":
        add_to_list()
    elif action == "r":
        remove_from_list()
    elif action == 'd':
        print_entire_list()
    elif action == "q":
        break
    else:
        print("\nAction not recognized.\n")