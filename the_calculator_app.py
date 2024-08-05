''' 
Objective: The aim of this assignment is to build a basic calculator that can perform addition,
subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
'''
def addition(a, b):
    print(f"{a} + {b} = {a + b}")

def subtraction(c, d):
    print(f"{c} - {d} = {c - d}")

def multiplication(e, f):
    print(f"{e} x {f} = {e * f}")

'''
Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
there is error handling set up to prevent an error from showing in the console.
'''

def division(g, h):
    if g and h != 0: 
        print(f"{g} ÷ {h} = {g / h}")
    else:
        print("indivisible")
'''
Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
'''
while True:
    print('Which operation would you like to perform?')
    choice = input(f"[A]ddition\n[S]ubtraction\n[M]ultiplication\n[D]ivision\n").lower()
    if choice in ["a", "d", "s", "m"]:
        number_1 = int(input("Enter first number (must be integer): "))     
        number_2 = int(input("Enter second number (must be integer): "))
        if choice == "a":
            addition(number_1, number_2)
        elif choice == 's':
            subtraction(number_1, number_2)
        elif choice == 'm':
            multiplication(number_1, number_2)
        elif choice == 'd':
            division(number_1, number_2)
        break
    else:
        choice = input("Choice not recognized. \n Would you like to quit or try again (q / any key)? ").lower()
        if choice == 'q':
            break

