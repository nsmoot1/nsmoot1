"""
ADD-100: Assignment 12A - The Configurable Menu & Auditor
Author: Nick Smoot
Date: 4/13/2026
File: menu_creator.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. PHASE 1: External menu_config.txt file created in workspace.
[x] 3. Program reads and parses the .txt file into a Dictionary.
[x] 4. PHASE 2: break the dictionary into individual variables.
[x] 6. Print each category and its details
[x] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""
# 1. --- Gets menu categories ---

def get_menu_options():
    menu = { }
    while True:
        print("Type 'Q' when done")
        category = input("Enter category: ").upper()
        if category == "Q":
            break
        items = input("Enter items seperated by commas: ")
        menu[category] = items
    return menu

# 2. --- Saves menu to menu_config.txt ---

def save_to_file(menu):
    with open ("menu_config.txt", "a") as file:
        all_items = menu.items()
        for item in all_items:
            output = (f"{item[0]}  : {item[1]}")
            file.write(output + "\n")

def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)

main()