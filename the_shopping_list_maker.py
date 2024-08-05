
''' 
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.

Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow 
the user to continue to add, remove, and print off their shopping list until 
they decide to "quit", also known as breaking the loop.
'''

def list_maker():
    shopping_list = []
    while True:
        action = input("What would you like to do?\n[A]dd item to list\n[R]emove item from list\n[D]isplay list\n[Q]uit\n").lower()
        if action == "a":
            item = input("Item to add: ").lower()
            shopping_list.append(item)
            print(f"\n{item} added to list\n")
        elif action == "r":
            item = input("Item to remove: ").lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"\n{item} removed from list\n")
            else:
                print(f"\n{item} not found in list\n")
        elif action == 'd':
            print("ITEMS:")
            if len(shopping_list) == 0:
                print("No items in list\n") 
            else:
                for item in shopping_list:
                    print(f"- {item}")
        elif action == "q":
            break

list_maker()
